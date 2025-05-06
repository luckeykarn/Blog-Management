from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from account.role_check_decorator_authorization import role_required
from blogs.models import Blogs
from comment.models import Comment
from django.core.paginator import Paginator
from django.http.response import HttpResponse,JsonResponse
from django.db.models import Q #this is imported for search function
from taggit.models import Tag # for tag 

@login_required
def author_dashboard(request):
    user = request.user
    blog_count = Blogs.objects.filter(author=user).count()
    comment_count = Comment.objects.filter(blog__author=user).count()
    recent_drafts = Blogs.objects.filter(author=user, status='draft').order_by('-created_at')[:5]

    return render(request, 'author_dashboard.html', {
        'blog_count': blog_count,
        'comment_count': comment_count,
        'recent_drafts': recent_drafts,
    })
