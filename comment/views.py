from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Blogs


@login_required
def create_comment(request, blog_slug):
    print(request.POST)
    print(blog_slug," b m")
    blog = Blogs.objects.get(slug=blog_slug)  # Fetch Blog by slug
    print(blog, " blog vetyo")
    if request.method == 'POST':
        print("in POST check")
        body = request.POST.get('body')
        if body:
            print(" in body")
            comment = Comment.objects.create(
                blog=blog,
                user=request.user,
                # Remove redundant name and email if you have a User ForeignKey
                # name=request.user.username,
                # email=request.user.email,
                body=body,
                approved=False  # Set approved to False for moderation
            )  
            # print(comment, " create vayo ki vayena?")     
            return redirect('blog_detail', slug=blog.slug)  # Redirect to the correct blog detail URL name
        else:
            return render(request, 'create_comments.html', {'error': 'Comment body is required.', 'blog': blog})

    return render(request, 'create_comments.html', {'blog': blog})


def comment_view(request):
    comments = Comment.objects.all().filter(approved=True).order_by('-created_at')
    context = {'comments': comments}
    return render(request, 'view_comments.html', context) 