from django.shortcuts import render , redirect
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.changed_data['password1']
            user = authenticate(username = username , password = password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request,"registration/signup.html",{'form':form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm()
        profile_form = ProfileForm()
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'profile/profile_edit.html', 
    {
    'user_form':user_form , 
    'prfile_form':profile_form
    }
    )
