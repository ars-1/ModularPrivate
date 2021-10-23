from django.forms import ModelForm, DateField, widgets
from .models import *


#######################################################################################################################
#######################################################################################################################

class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DesignationForm(ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'datestamp': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }


#######################################################################################################################
#######################################################################################################################

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'datestamp': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class BillingForm(ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
        widgets = {
            'datestamp': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }


