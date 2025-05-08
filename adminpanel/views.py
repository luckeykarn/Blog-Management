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


@login_required
def author_dashboard(request):
    # Get the selected status from the dropdown (default: published)
    selected_status = request.GET.get('status', 'published')

    # Filter blogs based on current user and selected status
    blogs = Blogs.objects.filter(
        author=request.user, 
        status=selected_status
    ).order_by('-created_at')

    # Pass data to the template
    context = {
        'blogs': blogs,
        'selected_status': selected_status,
    }
    return render(request, 'author_dashboard.html', context)


def categories(request):
    return render(request, 'categories.html')
    


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
        all_blogs = all_blogs.filter(category__iexact=category_filter)

    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter and status_filter in ['published', 'draft', 'pending', 'archived']:
        all_blogs = all_blogs.filter(status=status_filter)

    # Order the posts
    all_blogs = all_blogs.order_by('-created_at')

    # Pagination
    paginator = Paginator(all_blogs, 10)  # 10 posts per page
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


def setting(request):
    return render(request, 'setting.html')


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
            return render(request, "create_blog.html", context)
            
    elif request.method == "GET":
        categories = Category.objects.all()
        context = {
                    "categories":categories,
            }
        return render(request, 'add-post.html',context)

   