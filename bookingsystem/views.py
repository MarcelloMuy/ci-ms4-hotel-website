from django.shortcuts import render, HttpResponse
from .models import Bookings



def display_base(request):
    return render(request, '/workspace/ci-ms4-hotel-website/templates/base.html')
