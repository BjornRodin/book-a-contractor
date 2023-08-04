from . import views
from django.urls import path

"""
All paths needed to navigate
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('my-bookings/', views.my_bookings, name='my-bookings'),
    path('booking-form/', views.booking_form, name='booking-form'),
    path('booking-form/<int:pk>/', views.booking_form, name='booking-form'),
    path('view-booking/<int:pk>/', views.view_booking, name='view-booking'),
    path('delete-booking/<int:pk>/', views.delete_booking, name='delete-booking'),
    path('update-booking/<int:pk>/', views.update_booking, name='update-booking'),
]

handler404 = views.handler404