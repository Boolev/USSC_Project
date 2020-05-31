from django.shortcuts import render


def index(request):
    return render(request, 'requests_status/requests_status.html')
