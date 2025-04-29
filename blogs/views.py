from django.shortcuts import render

# Create your views here.
def my_blogs(request):
    context = {"title":"Blog title","user":request.user}
    return render(request,"blogs.html",context)