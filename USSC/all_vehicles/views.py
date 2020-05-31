from django.shortcuts import render
from .models import Vehicle
from .filters import VehicleFilter


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        vehicle_list = Vehicle.objects.filter(type__icontains=search_query)
    else:
        vehicle_list = Vehicle.objects.all()

    myFilter = VehicleFilter(request.GET, queryset=vehicle_list)
    vehicle_list = myFilter.qs

    context = {
        'vehicle_list': vehicle_list,
        'myFilter': myFilter
    }
    return render(request, 'all_vehicles/all_vehicles.html', context)
