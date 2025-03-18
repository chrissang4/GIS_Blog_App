from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("blog:blog_list")
        else:
            messages.error(request, "Error creating account")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog:blog_list")
        else:
            messages.error(request, "Error logging in")
            
    else:
        form = AuthenticationForm()
        
    return render(request, "registration/login.html", {"form": form})

def user_logout(request):
    logout(request)
    redirect("users:login")