from django.shortcuts import render
from destinations.models import Destination, Category

def home(request):
    destinations = Destination.objects.all().order_by('-pub_date')[:3]
    print destinations

    return render(request, "home.html", {
        'destinations': destinations
    })

