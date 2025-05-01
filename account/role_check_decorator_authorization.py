# accounts/decorators.py

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'role') and request.user.role in required_role:
                return view_func(request, *args, **kwargs)
            return redirect('permission_error')  # Create this view or use any fallback
        return _wrapped_view
    return decorator
