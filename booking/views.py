from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
from datetime import datetime

def index(request):
    return render(request, 'index.html')

@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'user_bookings': user_bookings})

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your Session has successfully been booked.')
            return redirect('my-bookings')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})