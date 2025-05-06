from django import template
from blogs.models import BlogLike  # Assuming BlogLike is in blogs.models

register = template.Library()  # Define register only once

@register.simple_tag
def get_blog_like_count(blog):
    # print(blog," lol")
    try:
        return blog.blog_like.count()
    except:
        return 0

@register.simple_tag
def is_blog_liked_by_user(user, blog):
    return BlogLike.objects.filter(blog=blog,user=user).exists()
 

@register.filter
def has_user_liked(blog, user):
    if user.is_authenticated:
        return BlogLike.objects.filter(blog=blog, user=user).exists()
    return False