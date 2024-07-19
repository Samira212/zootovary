from django_filters.rest_framework import FilterSet
from .models import Cat


class CatFilter(FilterSet):
    class Meta:
        model = Cat
        fields = {
            'name': ['exact'],
            'age': ['gt', 'lt'],
        }
