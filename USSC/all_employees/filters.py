import django_filters
from .models import Person

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['profession', 'object_name', 'violation_points']
