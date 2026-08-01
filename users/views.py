from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.models import EmailAddress
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  get_user_model
from django.contrib import messages
from .forms import ProfileForm, EmailForm

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


@login_required
def profile_email_change(request):
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if the email already exists
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')
            
            form.save() 
            
            # When using email confirmation locally in terminal, remove the = in the confirmation link!
            email_address = EmailAddress.objects.get(user=request.user, email=request.user.email)
            email_address.send_confirmation(request)
            
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Form not valid')
            return redirect('profile-settings')
        
    return redirect('home')


@login_required
def profile_email_verify(request):
    email_address = EmailAddress.objects.get(user=request.user, email=request.user.email)
    email_address.send_confirmation(request)
    return redirect('profile-settings')
