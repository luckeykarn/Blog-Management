from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from account.role_check_decorator_authorization import role_required
from blogs.models import Blogs
from comment.models import Comment
from django.core.paginator import Paginator
from django.http.response import HttpResponse,JsonResponse
from django.db.models import Q #this is imported for search function
from taggit.models import Tag # for tag 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from adminpanel.models import Category
from django.http import Http404, JsonResponse


@login_required
def author_dashboard(request):
    # Get filter status from query param, default = ''
    selected_status = request.GET.get('status', '')

    # Start with all blogs by current user
    blogs = Blogs.objects.filter(author=request.user).order_by('-created_at')

    # Apply status filter only if one is selected
    if selected_status in ['published', 'draft', 'pending', 'archived']:
        blogs = blogs.filter(status=selected_status)

    # Optional: count published and draft posts
    published_count = blogs.filter(status='published').count()
    draft_count = blogs.filter(status='draft').count()

    context = {
        'blogs': blogs,
        'selected_status': selected_status,
        'published_count': published_count,
        'draft_count': draft_count,
        'include_navbar': True,  # Flag to control navbar inclusion
    }
    return render(request, 'author_dashboard.html', context)


@login_required
def author_blog(request):
    
    # Get all posts for the current user
    all_blogs = Blogs.objects.filter(author=request.user)

    # Search
    query = request.GET.get('query', '')
    if query:
        all_blogs = all_blogs.filter(Q(title__icontains=query) | Q(category__name__icontains = query) )

    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        all_blogs = all_blogs.filter(category__name__iexact=category_filter)  # Filtering based on related Category model's name

    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter and status_filter in ['published', 'draft', 'pending', 'archived']:
        all_blogs = all_blogs.filter(status=status_filter)

    # Order the posts
    all_blogs = all_blogs.order_by('-created_at')

    # Pagination
    paginator = Paginator(all_blogs, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get unique categories for the dropdown
    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,  # Use 'page_obj' to be consistent with class-based view
        'query': query,
        'status_filter': status_filter,
        'category_filter': category_filter,
        'categories': categories,
    }

    return render(request, 'author_blogs.html', context)


    # query = request.GET.get('query', '')
    # status = request.GET.get('status', '')

    # posts = Blogs.objects.filter(author=request.user)

    # if query:
    #     posts = posts.filter(title__icontains=query)
    
    # if status:
    #     posts = posts.filter(status=status)

    # return render(request, 'author_blogs.html', {
    #     'posts': posts,
    #     'query': query,
    #     'status': status,
    # })


# def setting(request):
#     return render(request, 'setting.html')


def add_post(request):
    if request.method == "POST":
        try:
            # Get data from POST request
            title = request.POST.get('title')
            slug = request.POST.get('slug')
            content = request.POST.get('content')
            cover_image = request.FILES.get('cover_image')  # Changed to FILES for file uploads
            author = request.user  # Assuming author is the logged-in user
            status = request.POST.get('status')
            tags = request.POST.get('tags')
            
            # Create blog post
            blog = Blogs.objects.create(
                title=title,
                slug=slug,
                content=content,
                cover_image=cover_image,
                author=author,
                status=status,
                tags=tags
                # created_at and updated_at will be auto-set if auto_now_add and auto_now are True in model
            )
            print("created",blog)
            messages.success(request, 'Blog created successfully!')
            return redirect('author_blog')  # Or another appropriate redirect
            
        except Exception as e:
            messages.error(request, f'Error creating blog: {str(e)}')
            # Return to form with existing data if you want to implement that
            context = {
                "title": request.POST.get('title'),
                "content": request.POST.get('content'),
                "slug": request.POST.get('slug'),
                "user": request.user,
                "error": str(e)
            }
            return render(request, 'add-post.html',context)
            
    elif request.method == "GET":
        categories = Category.objects.all()
        context = {
                    "categories":categories,
            }
        return render(request, 'add-post.html',context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def profile_settings(request):
    user = request.user
    
    if request.method == 'POST':
        # Handle profile picture upload
        if 'profile_picture' in request.FILES:
            # Remove old profile picture if exists
            if user.profile_picture:
                user.profile_picture.delete()
            user.profile_picture = request.FILES['profile_picture']
        
        # Update profile fields
        user.first_name = request.POST.get('display_name', '').split()[0] if request.POST.get('display_name') else ''
        user.last_name = ' '.join(request.POST.get('display_name', '').split()[1:]) if request.POST.get('display_name') else ''
        user.bio = request.POST.get('bio', '')
        user.gender = request.POST.get('gender')
        
        # Update email if changed
        new_email = request.POST.get('email')
        if new_email and new_email != user.email:
            user.email = new_email
        
        # Handle notification preferences
        user.notify_comments = 'notify_comments' in request.POST
        user.notify_replies = 'notify_replies' in request.POST
        user.notify_mentions = 'notify_mentions' in request.POST
        user.notify_followers = 'notify_followers' in request.POST
        user.push_comments = 'push_comments' in request.POST
        user.push_replies = 'push_replies' in request.POST
        
        # Handle social media and sharing preferences
        user.twitter_handle = request.POST.get('twitter', '')
        user.facebook_url = request.POST.get('facebook', '')
        user.instagram_handle = request.POST.get('instagram', '')
        user.linkedin_url = request.POST.get('linkedin', '')
        user.github_handle = request.POST.get('github', '')
        user.share_twitter = 'share_twitter' in request.POST
        user.share_facebook = 'share_facebook' in request.POST
        user.share_linkedin = 'share_linkedin' in request.POST
        
        try:
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_settings')
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
    
    context = {
        'user': user,
    }
    return render(request, 'profile_settings.html', context)


# @login_required
# def published_post(request):

#     # Only show published blogs for the logged-in user
#     blog_list = Blogs.objects.filter(author=request.user, status='published').order_by('-id')

#     context = {
#         "title": "My Blogs",
#         "user": request.user,
#         "blogs": blog_list  # Pass the blog list to the template
#     }

#     return render(request, "author_dashboard.html", context)


@login_required
def categories(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        if name:
            if Category.objects.filter(name__iexact=name).exists():
                messages.error(request, 'Category already exists.')
            else:
                Category.objects.create(name=name)
                messages.success(request, 'Category added successfully.')
                return redirect('categories')
        else:
            messages.error(request, 'Category name is required.')

    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


@login_required
def update_category(request):
    if request.method == 'POST':
        try:
            cat_id = request.POST.get('id')
            name = request.POST.get('name', '').strip()

            if not cat_id:
                return JsonResponse({'success': False, 'error': 'Category ID is required'}, status=400)
            
            if not name:
                return JsonResponse({'success': False, 'error': 'Category name cannot be empty'}, status=400)

            # Check if category exists
            category = Category.objects.filter(id=cat_id).first()
            if not category:
                return JsonResponse({'success': False, 'error': 'Category not found'}, status=404)

            # Check for duplicate names (case-insensitive, excluding current category)
            if Category.objects.filter(name__iexact=name).exclude(id=cat_id).exists():
                return JsonResponse({'success': False, 'error': 'A category with this name already exists'}, status=400)

            # Update the category
            category.name = name
            category.save()
            
            return JsonResponse({'success': True})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

@login_required
def delete_category(request):
    if request.method != 'POST':
        return JsonResponse({
            'success': False,
            'error': 'Only POST requests are allowed'
        }, status=405)

    cat_id = request.POST.get('id')
    if not cat_id:
        return JsonResponse({
            'success': False,
            'error': 'Category ID is required'
        }, status=400)

    try:
        category = get_object_or_404(Category, id=cat_id)
        category.delete()
        return JsonResponse({'success': True})
        
    except Http404:
        return JsonResponse({
            'success': False,
            'error': 'Category not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


def navbar(request):
    return render(request, "navbar.html")

def profile_view(request):
    return render(request, "profile_view.html")

def post_edit(request,id):
    blog_id = id
    print("blog_id",blog_id)
    blog_object = Blogs.objects.get(id = blog_id)
    if request.method == "POST":
        print(request.POST)
        blog_object.title = request.POST["title"]
        blog_object.slug = request.POST["slug"]
        blog_object.content = request.POST["content"]
        blog_object.category = Category.objects.get(id=request.POST["category"])
        blog_object.tags = request.POST["tags"]
        blog_object.status = request.POST["status"]
        blog_object.cover_image = request.FILES["cover_image"]
        blog_object.save()

        #use update method
        # pass
        return HttpResponse("blog updated success")
    else:
        context = {
            "blog":blog_object,
            "categories":Category.objects.all()
        }
        return render (request,"post_edit.html",context)