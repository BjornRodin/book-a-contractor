from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

@login_required
def my_bookings(request):
    return render(request, 'my_bookings.html')

def register(request):
    return render(request, 'register.html')

def login_user(request):
    return render(request, 'login.html')

@login_required
def booking_form(request):
    return render(request, 'booking_form.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('booking-form')