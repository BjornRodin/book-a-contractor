from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('my-bookings/', views.my_bookings, name='my-bookings'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('booking-form/', views.booking_form, name='booking-form'),
    path('view-booking/<int:pk>/', views.view_booking, name='view-booking'),
    path('delete-booking/<int:pk>/', views.delete_booking, name='delete-booking'),
]