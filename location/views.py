from django.shortcuts import render
from . import utilities

def landing(request):
    return render(request, "location/landing.html")

    
def home(request):
    if request.method == "POST":
        address = request.POST.get('address')
        location = utilities.location_by_address(address)
        context = {
            'latitude':location['lat'],
            'longitude':location['lon']
        }
        return render(request, "location/home.html",context)
    return render(request, "location/home.html")

def index(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        context = {
            'address':utilities.address_by_location(latitude, longitude)
        }
        return render(request, "location/index.html",context)
    return render(request, "location/index.html")