from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def author_required(view_func):
    @wraps(view_func)  # Preserves the original function's metadata
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please login to access this page")
            return redirect('user_login')
            
        if not hasattr(request.user, 'profile'):
            messages.error(request, "User profile not found")
            return redirect('profile_complete')  # Redirect to profile creation
            
        if not (request.user.profile.is_author or request.user.is_staff):
            messages.error(request, "Author privileges required")
            return redirect('my-blogs')
            
        return view_func(request, *args, **kwargs)
    return wrapper

def reader_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please login to access this page")
            return redirect('user_login')
            
        if not hasattr(request.user, 'profile'):
            messages.error(request, "User profile not found")
            return redirect('profile_complete')
            
        if not request.user.profile.is_reader:
            messages.error(request, "Reader account required")
            return redirect('upgrade_account')  # Specific page for readers
            
        return view_func(request, *args, **kwargs)
    return wrapper