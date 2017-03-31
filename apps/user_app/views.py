from django.shortcuts import render, redirect, HttpResponse
import re
from .models import User
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'user_app/login.html')


def register(request):
    server_name = request.POST['name']
    server_username = request.POST['username']
    server_password = request.POST['password']
    server_confirm = request.POST['confirm_password']
    server_hiredate = request.POST['date_of_hire']
    if len(server_name) < 3:
        messages.error(request, 'ERROR: Name should be at least 3 characters!')
        return redirect('user:login')
    if len(server_username) < 3:
        messages.error(request, 'ERROR: Username should be at least 3 characters!')
        return redirect('user:login')
    if len(server_password) < 8:
        messages.error(request, 'ERROR: Password should be at least 8 characters!')
        return redirect('user:login')
    if server_password == server_confirm:
        try:
            user = User.objects.create(name=server_name, username=server_username, password=server_password, hire_date=server_hiredate)
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            return redirect('wishlist:home')
        except:
            messages.error(request, 'ERROR: Email already exists!')
            return redirect('user:login')
    else:
        messages.add_message(request, messages.ERROR, 'ERROR: Passwords do not match!')
        return redirect('user:login')


def authenticate(request):
    server_username = request.POST['username']
    server_password = request.POST['password']
    try:
        user = User.objects.get(username=server_username)
        if user.password == server_password:
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            return redirect('wishlist:home')
    except:
        messages.add_message(request, messages.ERROR, 'ERROR: Email does not exist!')
    messages.add_message(request, messages.ERROR, 'ERROR: Password invalid, try again!')
    return redirect('user:login')


def logout(request):
    request.session.clear()
    return redirect('user:login')
