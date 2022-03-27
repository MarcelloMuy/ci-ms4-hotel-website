"""myhotelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookingsystem.views import (
    display_bookings, display_home, book_now, update_booking, cancel_booking)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mybookings/', display_bookings, name='mybookings'),
    path('', display_home, name='homepage'),
    path('booknow/', book_now, name='booknow'),
    path('update/<booking_id>', update_booking, name='update'),
    path('cancel/<booking_id>', cancel_booking, name='cancel')
    ]
