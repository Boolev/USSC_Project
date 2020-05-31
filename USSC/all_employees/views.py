from django.shortcuts import render
from .models import Person
from .filters import PersonFilter
from django.db.models import Q

def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        employees_list = Person.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(patronymic__icontains=search_query))
    else:
        employees_list = Person.objects.all()

    myFilter = PersonFilter(request.GET, queryset=employees_list)
    violation_list = myFilter.qs

    context = {
        'employees_list': employees_list,
        'myFilter': myFilter,
    }
    return render(request, 'all_employees/all_employees.html', context)
