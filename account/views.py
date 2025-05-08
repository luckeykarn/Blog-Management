from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import CustomUser as User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
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
        hash_password = make_password(password)
        User.objects.create(username=username,email=email,password=hash_password)
        return redirect('user_login')
    
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
            return redirect('my-blogs')

        else:
            return HttpResponse("Your username/password is incorrect")
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('my-blogs')

def profile(request):
   return render(request, 'profile.html')

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


def permission_error(request):
    # This view can only be accessed by Authors or Admins
    return render(request, 'permission_error.html')

