from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
from datetime import datetime

"""
Renders index (landing page), register and login for none-authorized users
"""
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

"""
Renders a 404 error-page if a 404 error occurs
"""
def handler404(request, exception):
    return render(request, '404.html', status=404)

"""
Renders my bookings, booking form, view booking, delete booking, update booking
for authorized users only.
"""

@login_required
def my_bookings(request):
    """
    Check if there is any existing bookings for the logged in user, then renders page with content
    """
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'user_bookings': user_bookings})

@login_required
def booking_form(request, pk=None):
    """
    Handle creation of new bookings
    """
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

@login_required
def view_booking(request, pk):
    """
    Find the booking the user click on and renders it with all its information
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'view_booking.html', {'booking': booking})

@login_required
def delete_booking(request, pk):
    """
    Get the booking the user want to delete
    If deleted user is presented with a message
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'You have successfully deleted your booked session.')
        return redirect('my-bookings')
    return render(request, 'delete_booking.html', {'booking': booking})

@login_required
def update_booking(request, pk):
    """
    Handle updates of existing booked sessions
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booked session was successfully updated.')
            return redirect('my-bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'update_booking.html', {'form': form})
