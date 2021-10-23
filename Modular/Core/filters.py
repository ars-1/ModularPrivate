from django.db.models import fields
import django_filters
from django_filters import DateFilter
from Oracle.models import *
from django.forms import widgets


#######################################################################################################################
class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['fname', 'lname', 'mobile', 'department']


class AttendanceFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name="datestamp", lookup_expr='gte',
                           widget=widgets.DateInput(attrs={'type': 'date'}))
    enddate = DateFilter(field_name="datestamp", lookup_expr='lte', widget=widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Attendance
        fields = ['employee', 'status', 'month']
        widgets = {
            'datestamp': widgets.DateInput(attrs={'type': 'date'})
        }
