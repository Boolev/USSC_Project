from django.shortcuts import render


def index(request):
    return render(request, 'add_employee/add_employee.html')
