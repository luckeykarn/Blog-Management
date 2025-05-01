from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from .decorators import author_required
from .models import Profile
from .decorators import author_required



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
        return redirect('user_login')
    
    else:
        return render(request, 'register.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Profile  # make sure to import your Profile model

def user_login(request):
    if request.method == 'POST':
        # Make sure to include csrf_token in your template form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Create profile if it doesn't exist
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('my-blogs')  # make sure 'my-blogs' is a valid URL name
        else:
            # Return to login page with error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    # GET request - show login form
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return HttpResponse("You are loged out successfulley!!!")

def profile(request):
   return render(request, 'profile.html')

# def Profile_Update(request):
#     if request.method == 'POST':
#         form_username = request.POST["username"]
#         form_email = request.POST["email"]
#         form_password = request.POST["password"]
#         print(form_username,form_email)
#         user_object = request.user
#         print(user_object)
#         user_object.username = form_username
#         user_object.email = form_email
#         if len(form_password)>2:
#             user_object.password = make_password(form_password)

#         user_object.save()
#         return HttpResponse("Profile Updated successfulley!!!")
    
#      # Handle GET request: render the form
#     return render(request, "profile_update.html", {
#         "user": request.user
#     })

def Profile_Update(request):
    if request.method == 'POST':
        form_username = request.POST["username"]
        form_email = request.POST["email"]
        form_password = request.POST["password"]

        user_object = request.user
        user_object.username = form_username
        user_object.email = form_email

        if len(form_password) > 2:
            user_object.password = make_password(form_password)

        user_object.save()
        return HttpResponse("Profile updated successfully!")

    # Handle GET request: render the form
    return render(request, "profile_update.html", {
        "user": request.user
    })


# from django.shortcuts import render
# from .decorators import author_required

@author_required
def create_post(request):
    # this view only can be accessed by authors and admin
    return render(request, 'create_post.html')