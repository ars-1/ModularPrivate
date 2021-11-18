from django.shortcuts import render, redirect
from .models import *
import datetime
from django.utils import timezone as tz
from Core.filters import *
from .forms import *
from .employeeViews import *
from django.contrib.auth.decorators import login_required
from Guardian.decorators import admin_only



@login_required(login_url='/guardian/login/')
@admin_only
def ClientL(request):
    clients = Client.objects.all()
    billings = Billing.objects.all()
    context = {
        'clients': clients,
        'billings': billings,
    }
    return render(request, 'Oracle/Billing/clients.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def BillingL(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'Oracle/Billing/billing.html', context)

@login_required(login_url='/guardian/login/')
def ClientDetails(request, pk):
    client = Client.objects.get(id=pk)
    collectedBills = Billing.objects.filter(client__id__contains=pk)
    context = {
        'client': client,
        'bills': collectedBills,
    }
    return render(request, 'Oracle/Billing/ClientDetails.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def AddClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/oracle/clients/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Billing/AddClient.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def UpdateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/oracle/clients/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Billing/UpdateClient.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def DeleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/oracle/clients/')
    context = {
        'client': client,
    }
    return render(request, 'Oracle/Billing/DeleteClient.html', context)

#######################################################################################################################
#######################################################################################################################
@login_required(login_url='/guardian/login/')
def BillDetails(request, pk):
    bill = Billing.objects.get(id=pk)
    context = {
        'bill': bill,
    }
    return render(request, 'Oracle/Billing/BillDetails.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def AddBill(request, pk):
    client = Client.objects.get(id=pk)
    form = BillingForm(initial={'client': client.username})
    dueForm = DueForm(instance=client)
    if request.method == 'POST':
        form = BillingForm(request.POST)
        dueForm = DueForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            dueForm.save()
            return redirect('/oracle/billing/')
    context = {
        'client': client,
        'form': form,
        'dueForm': dueForm,
    }
    return render(request, 'Oracle/Billing/AddBill.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def UpdateBill(request, pk):
    bill = Billing.objects.get(id=pk)
    form = BillingForm(instance=bill)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect(request, '/oracle/billing/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Billing/UpdateBill.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def DeleteBill(request, pk):
    bill = Billing.objects.get(id=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('/oracle/billing/')
    context = {
        'bill': bill,
    }
    return render(request, 'Oracle/Billing/DeleteBill.html', context)