from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  get_user_model
from .forms import ProfileForm

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


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user)  
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    onboarding = request.path == reverse('profile-onboarding')

    return render(request, 'users/profile_edit.html', {'form': form, 'onboarding': onboarding})


@login_required
def profile_settings_view(request):
    return render(request, 'users/profile_settings.html')
