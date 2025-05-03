from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.role_check_decorator_authorization import role_required
from .models import Blogs
from django.core.paginator import Paginator

# Create your views here.
# @role_required(["admin","user"])
# @login_required
def my_blogs(request):
    page_number = request.GET.get('page')
    blog_list = Blogs.objects.all()  # Optional: order by newest

    paginator = Paginator(blog_list, 2)  # 2 blogs per page
    # print(paginator.num_pages) #this give number of pages
    # print(paginator.__dict__)

    page_obj = paginator.get_page(page_number)

    # for blog in page_obj:
    #     print(blog)


    context = {
        "title": "Blog title",
        "user": request.user,
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
        # GET request - show empty form
        # context = {
        #     "title": "Create New Blog",
        #     "user": request.user
        # }
        # return render(request, "create_blog.html", context)

        blogs = Blogs.objects.filter(author=request.user)  # shows only logged-in user's blogs
    context = {
        "title": "My Blogs",
        "user": request.user,
        "blogs": blogs
    }
    return render(request, "create_blog.html", context)


# @role_required(["author"])
# def create_blog(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         slug = request.Post['slug']
#         content = request.POST['content']
#         cover_image = request.POST['cover_image'] 
#         author = request.POST['author']
#         # created_at = request.POST['created_at']
#         # updated_at = request.POST['updated_at']
#         status = request.POST['status']
#         tags = request.POST['tags']
#         created_at = request.POST['created_at']
#         updated_at = request.POST['updated_at']
#         Blogs.objects.create(title=title,slug="slug",content="content",cover_image="cover_image",author="author",status ="status",tags="tags",created_at="created_at",updated_at="updated_at")


#         context = {"title":"Blog title","user":request.user}
#         return render(request,"create_blog.html",context)
#         # return redirect back with saved successsfully message
#     else:
#         context = {"title":"Blog title","user":request.user}
#         return render(request,"create_blog.html",context)

def blog_detail(request):
    blog_slug = request.GET.get('slug')
    print(blog_slug," blog slug")

    blog_object = Blogs.objects.get(slug=blog_slug) # Optional: order by newest

    # for blog in page_obj:
    #     print(blog)


    context = {
        "title": "Blog title",
        "user": request.user,
        "blog":blog_object,
      
    }

    return render(request, "blog_detail.html", context)