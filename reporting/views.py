from django.shortcuts import render, redirect
from reports.forms import ReportForm
from reports.models import Resource
from reports.models import Location
from reports.forms import ResourceForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import haversine





def report_create_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_success')  # Redirect to the success page after form submission
    else:
        form = ReportForm()

    return render(request, 'report.html', {'form': form})

def report_success_view(request):
    return render(request, 'succes.html')

def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})
def add_resource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')  # Redirect to the resources list page
    else:
        form = ResourceForm()
    return render(request, 'add_resource.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def save_location(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        user_lat = data.get('latitude')
        user_lon = data.get('longitude')

        if not user_lat or not user_lon:
            return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)

        # Fetch all locations from the database
        locations = Location.objects.all()

        # Check if there are any locations available
        if not locations.exists():
            return JsonResponse({'error': 'No locations available in the database'}, status=404)

        # Find the nearest location using haversine formula
        nearest_location = min(
            locations,
            key=lambda loc: haversine(float(user_lat), float(user_lon), loc.latitude, loc.longitude)
        )

        # Return the nearest location's data
        return JsonResponse({
            'name': nearest_location.name,
            'latitude': nearest_location.latitude,
            'longitude': nearest_location.longitude
        })

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_nearest_location(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        user_lat = data.get('latitude')
        user_lon = data.get('longitude')

        if not user_lat or not user_lon:
            return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)

        # Fetch all stored locations
        locations = Location.objects.all()
        if not locations:
            return JsonResponse({'error': 'No locations available in the database'}, status=404)

        # Find the nearest location using the haversine function
        nearest_location = min(
            locations,
            key=lambda loc: haversine(float(user_lat), float(user_lon), loc.latitude, loc.longitude)
        )

        # Return the nearest location details
        return JsonResponse({
            'name': nearest_location.name,
            'latitude': nearest_location.latitude,
            'longitude': nearest_location.longitude,
            'distance': haversine(float(user_lat), float(user_lon), nearest_location.latitude, nearest_location.longitude)
        })

    return JsonResponse({'error': 'Invalid request method'}, status=405)