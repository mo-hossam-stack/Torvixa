from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  get_user_model

User = get_user_model()

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username)
    else:
        try:
            profile = request.user
        except:
            return redirect('account_login')
    return render(request, 'users/profile.html', {'profile':profile})
