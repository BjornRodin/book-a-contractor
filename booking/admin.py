from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Adds 'Bookings' to the admin panel where an admin can view all bookings
    Features added to view certain information in a list,
    Search for specific elements
    A filter to quickly check bookings within that filter
    And fields for textareas so they are more customizable and clearly
    visible when viewing a booking
    """
    list_display = (
        'first_name',
        'last_name',
        'email',
        'date',
        'time',
        'project_type'
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'project_type'
    )
    list_filter = (
        'first_name',
        'last_name',
        'email',
        'date',
        'time',
        'project_type'
    )
    summernote_fields = (
        'project_type',
        'project_details'
    )
