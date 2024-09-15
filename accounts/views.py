from django.shortcuts import render
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request,"registration/signup.html",{'form':form})

def profile(request):
    pass


def edit_profile(request):
    pass
