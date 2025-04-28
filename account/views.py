from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# from dja

# Create your views here.
def register(request):
    if request.method == 'POST':
        all_form_data = request.POST
        print(all_form_data)
        username = all_form_data['username']
        email = all_form_data['email']
        password = all_form_data['password']
        print("we are registering signup")
        User.objects.create(username=username,email=email,password=password)
        return HttpResponse("create user")
    
    else:
        return render(request, 'register.html')

def user_login(request):
    # print("method name:",request.method)
    if request.method == 'POST':
        # pass
        all_form_data = request.POST
        print(all_form_data)
        print("type of all_form_data",type(all_form_data))
        form_username = all_form_data['username']
        form_password = all_form_data['password']
        user = authenticate(request,username=form_username,password=form_password)
        # user = User.objects.get(username=form_username)
        # print("user object:",user.__dict__)
        # username = request.POST['username']
        # password = request.POST[]
        if user:
            login(request,user)
            return HttpResponse("You are loged in successfulley!!!")
        else:
            return HttpResponse("Your username/password is incorrect")
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return HttpResponse("You are loged out successfulley!!!")

