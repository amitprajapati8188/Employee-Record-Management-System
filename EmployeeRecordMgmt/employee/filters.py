# filters.py
import django_filters
from .models import EmployeeDetail

class EmployeeDetailFilter(django_filters.FilterSet):
    class Meta:
        model = EmployeeDetail
        fields = ['empdept', 'designation', 'salary', 'joiningdate']
