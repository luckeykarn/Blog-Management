from django.shortcuts import render

# Create your views here.
def my_blogs(request):
    return render(request,"blogs.html")