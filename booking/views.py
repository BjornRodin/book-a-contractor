from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import BookingForm, UpdateBookingForm
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

@login_required
def view_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'view_booking.html', {'booking': booking})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'You have successfully deleted your booked session.')
        return redirect('my-bookings')
    return render(request, 'delete_booking.html', {'booking': booking})

@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booked session was successfully updated.')
            return redirect('view-booking')
    else:
        form = UpdateBookingForm(instance=booking)
    return render(request, 'update_booking.html', {'form': form})