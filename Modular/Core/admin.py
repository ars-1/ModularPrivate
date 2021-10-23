from django.contrib import admin
from Oracle.models import *
# Register your models here.
RegisteredModels = [
    # Employees
    Employee,
    Designation,
    Department,
    Attendance,

    # Billing
    Package,
    Client,
    Billing,
]

admin.site.register(RegisteredModels)