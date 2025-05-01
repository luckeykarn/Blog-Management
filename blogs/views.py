from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.role_check_decorator_authorization import role_required
from .models import Blogs

# Create your views here.
# @role_required(["admin","user"])
# @login_required
def my_blogs(request):
    context = {"title":"Blog title","user":request.user}
    return render(request,"blogs.html",context)

@role_required(["author"])
def create_blog(request):
    if request.method == "POST":
        # title = request.POST['title']
        # Blogs.objects.create(title=title,slug="slug")


        context = {"title":"Blog title","user":request.user}
        return render(request,"create_blog.html",context)
        # return redirect back with saved successsfully message
    else:
        context = {"title":"Blog title","user":request.user}
        return render(request,"create_blog.html",context)