from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def my_bookings(request):
    return render(request, 'my_bookings.html')

def register(request):
    return render(request, 'register.html')

def login_user(request):
    return render(request, 'login.html')