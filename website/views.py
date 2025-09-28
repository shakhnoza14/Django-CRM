from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!!!!!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')
    else:
        return render(request, 'home.html')
    

def register_user(request):
    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.....')
    return redirect('home')

