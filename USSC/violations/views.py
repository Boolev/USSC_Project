from django.http import HttpResponse
from django.template import loader
from .models import Violation
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .filters import ViolationFilter
from django.views.generic.list import ListView


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        violation_list = Violation.objects.filter(violator_FIO__icontains=search_query)
    else:
        violation_list = Violation.objects.order_by('-date')

    myFilter = ViolationFilter(request.GET, queryset=violation_list)
    violation_list = myFilter.qs

    context = {
        'violation_list': violation_list,
        'myFilter': myFilter
    }
    return render(request, 'violations/index.html', context)


def detail(request, violation_id):
    violation = get_object_or_404(Violation, pk=violation_id)
    return render(request, 'violations/detail.html', {'violation': violation})