from django.shortcuts import render


def index(request):
    return render(request, 'add_vehicle/add_vehicle.html')
