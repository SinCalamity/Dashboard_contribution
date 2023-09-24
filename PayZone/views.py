from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home_page/home_web.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('PayZone:login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('PayZone:dashboard')  # Redirect to the dashboard or any other desired page
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'user_auth/login.html')

def dashboard(request):
    # Add your dashboard logic here
    return render(request, 'main_page/home_dashboard.html')