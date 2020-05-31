import django_filters
from .models import *

class ViolationFilter(django_filters.FilterSet):
    class Meta:
        model = Violation
        fields = ['type', 'violator_profession', 'object_name', 'date']
