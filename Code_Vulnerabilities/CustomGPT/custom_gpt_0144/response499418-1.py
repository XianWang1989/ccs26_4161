from itertools import groupby
from django.shortcuts import render
from .models import Car

def catalog(request):
    # Fetch all cars ordered by name
    all_cars = Car.objects.all().order_by('name')

    # Group cars by the 'name' field using itertools.groupby
    grouped_cars = {}
    for key, group in groupby(all_cars, lambda x: x.name):
        grouped_cars[key] = [car.model for car in group]

    # Pass the grouped cars to the template
    return render(request, 'index.html', {'cars': grouped_cars})
