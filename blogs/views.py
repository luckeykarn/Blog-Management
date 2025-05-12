from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from account.role_check_decorator_authorization import role_required
from .models import Blogs,BlogLike
from comment.models import Comment
from django.core.paginator import Paginator
from django.http.response import HttpResponse,JsonResponse
from django.db.models import Q #this is imported for search function
from taggit.models import Tag # for tag 
from django.contrib.auth.models import AnonymousUser #for AnonymousUser


# Create your views here.
# @role_required(["admin","user"])
# @login_required(login_url='user_login')
def my_blogs(request):
    page_number = request.GET.get('page')
    # print(request.user),Blogs.objects.all().first().author,"********************")
    # blog_list = Blogs.objects.all().filter(author = request.user).order_by('-id')  # Optional: order by newest
   
    if request.user.is_authenticated:
        # Show all posts (published and unpublished) for logged-in users
        blog_list = Blogs.objects.all().order_by('-id')  # All posts, regardless of status
    else:
        # For anonymous users, show only published posts
        blog_list = Blogs.objects.filter(status='published').order_by('-id')  # Published posts only

    paginator = Paginator(blog_list, 6)  # 6 blogs per page
    # print(paginator.num_pages) #this give number of pages
    # print(paginator.__dict__)

    page_obj = paginator.get_page(page_number)

    context = {
        "title": "Blog title",
        "user": request.user if request.user.is_authenticated else None,
        "blogs": page_obj,
        "total_pages":range(1,paginator.num_pages+1)
    }

    return render(request, "blogs.html", context)


from django.shortcuts import render, redirect
from django.contrib import messages

@role_required(["author","admin"])
def create_blog(request):
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
            
            messages.success(request, 'Blog created successfully!')
            return redirect('my-blogs')  # Or another appropriate redirect
            
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
            
    else:
        
        blogs = Blogs.objects.filter(author=request.user,status='published')  # shows only logged-in user's blogs
        context = {
            "title": "My Blogs",
            "user": request.user,
            "blogs": blogs
        }
        return render(request, "create_blog.html", context)


def blog_detail(request, slug): # Receive slug as a path parameter
    blog_object = Blogs.objects.get(slug=slug) # Use get_object_or_404 for safety
    comments = Comment.objects.filter(blog=blog_object).order_by('-created_at') # Fetch approved comments

    context = {
        "title": blog_object.title, # Use the actual blog title
        "user": request.user,
        "blog": blog_object,
        "comments": comments, # Include the comments in the context
    }
    return render(request, "blog_detail.html", context) # Make sure the template name is correct

# def dashboard(request):
#     return render(request,"dashboard_blog.html")


@login_required
def like_blog(request):
    if request.method == "GET":
        user = request.user
        blog_id = request.GET.get('blog_id')

        if blog_id:
            try:
                blog = get_object_or_404(Blogs, id=blog_id)

                # Check if the user has already liked this blog
                like, created = BlogLike.objects.get_or_create(user=user, blog=blog)

                if not created:
                    # If already liked, delete the like (for unliking)
                    like.delete()
                    liked = False
                else:
                    liked = True
                
                print(liked," liked *********")

                # Return a JSON response indicating success and the like status
                likes_count = BlogLike.objects.filter(blog=blog).count()
                return JsonResponse({'status': 'success', 'liked': liked, 'blog_id': blog.id, 'likes_count': likes_count})

            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Invalid blog_id'}, status=400)
            except Blogs.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Blog not found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing blog_id'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    
# search blog by title,content and tag
def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        results = Blogs.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct() if query else []

        error_message = ""
        if query and not results:
            error_message = f'No results found for "{query}".'

        return render(request, 'blogs.html', {
            'blogs': results,
            'query': query,
            'error_message': error_message
        })
# It shows tag
def blogs_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    blogs = Blogs.objects.filter(tags__in=[tag], status='published').distinct()
    
    return render(request, 'blogs.html', {
        'blogs': blogs,
        'tag': tag,
        'query': f'Tag: {tag.name}'
    })

