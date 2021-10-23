from django.shortcuts import render, redirect
from .models import *
import datetime
from django.utils import timezone as tz
from Core.filters import *
from .forms import *


def Employees(request):
    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    empFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = empFilter.qs
    attFilter = AttendanceFilter(request.GET, queryset=attendances)
    attendances = attFilter.qs
    context = {
        'employees': employees,
        'attendances': attendances,
        'empFilter': empFilter,
        'attFilter': attFilter,
    }
    return render(request, 'Oracle/Employee/Employees.html', context)


def EmployeeDetails(request, pk):
    employee = Employee.objects.get(id=pk)
    attendances = Attendance.objects.filter(employee__id__contains=pk)
    d = tz.now() - datetime.timedelta(days=30)
    d2 = tz.now() + datetime.timedelta(days=1)

    presents = Attendance.objects.filter(
        status__contains='Present',
        datestamp__gt=d,
        datestamp__lte=d2,
        employee__id__contains=pk).count()
    absents = Attendance.objects.filter(
        status__contains='Absent',
        datestamp__gt=d,
        datestamp__lte=d2,
        employee__id__contains=pk).count()
    leaves = Attendance.objects.filter(
        status__contains='Leave',
        datestamp__gt=d,
        datestamp__lte=d2,
        employee__id__contains=pk).count()
    halftimes = Attendance.objects.filter(
        status__contains='Half Time',
        datestamp__gt=d,
        datestamp__lte=d2,
        employee__id__contains=pk).count()

    BasicSalary = employee.salary
    absentsCut = (BasicSalary/30) * absents
    FinalSalary = BasicSalary - absentsCut

    context = {
        'employee': employee,
        'attendances': attendances,
        'fromd': d,
        'tod': d2,

        'presents': presents,
        'absents': absents,
        'halftimes': halftimes,
        'leaves': leaves,

        'Salary': FinalSalary,
    }
    return render(request, 'Oracle/Employee/EmployeeDetails.html', context)


def AddEmployee(request):
    form = AddEmployeeForm()
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/oracle/employees/')
        else:
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Employee/AddEmployee.html', context)

def UpdateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = AddEmployeeForm(instance=employee)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/oracle/employees/')
    context = {
        'form': form,
        'employee': employee,
    }
    return render(request, 'Oracle/Employee/UpdateEmployee.html', context)

def DeleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('/oracle/employees/')
    context = {
        'employee': employee,
    }
    return render(request, 'Oracle/Employee/DeleteEmployee.html', context)

#######################################################################################################################
#######################################################################################################################

def AddAttendance(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/oracle/employees/')
    context = {
        'form': form
    }
    return render(request, 'Oracle/Employee/AddAttendance.html', context)

def UpdateAttendance(request, pk):
    attendance = Attendance.objects.get(id=pk)
    form = AttendanceForm(instance=attendance)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('/oracle/employees/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Employee/UpdateAttendance.html', context)

def DeleteAttendance(request, pk):
    attendance = Attendance.objects.get(id=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('/oracle/employees/')
    context = {
        'attendance': attendance,
    }
    return render(request, 'Oracle/Employee/DeleteAttendance.html', context)

#######################################################################################################################
#######################################################################################################################

def AddDesignation(request):
    form = DesignationForm()
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/oracle/employees/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Employee/AddDesignation.html', context)
def AddDepartment(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/oracle/employees/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Employee/AddDepartment.html', context)