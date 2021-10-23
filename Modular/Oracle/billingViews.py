from django.shortcuts import render, redirect
from .models import *
import datetime
from django.utils import timezone as tz
from Core.filters import *
from .forms import *
from .employeeViews import *




def ClientL(request):
    clients = Client.objects.all()
    billings = Billing.objects.all()
    context = {
        'clients': clients,
        'billings': billings,
    }
    return render(request, 'Oracle/Billing/clients.html', context)


def ClientDetails(request, pk):
    client = Client.objects.get(id=pk)
    collectedBills = Billing.objects.filter(client__id__contains=pk)
    context = {
        'client': client,
        'bills': collectedBills,
    }
    return render(request, 'Oracle/Billing/ClientDetails.html', context)


def AddClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/oracle/billing/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Billing/AddClient.html', context)

def UpdateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/oracle/billing/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Billing/UpdateClient.html', context)

def DeleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/oracle/billing')
    context = {
        'client': client,
    }
    return render(request, 'Oracle/Billing/DeleteClient.html', context)

#######################################################################################################################
#######################################################################################################################
def BillDetails(request, pk):
    bill = Billing.objects.get(id=pk)
    context = {
        'bill': bill,
    }
    return render(request, 'Oracle/Billing/BillDetails.html', context)

def AddBill(request, pk):
    client = Client.objects.get(id=pk)
    form = BillingForm(initial={'client': client.username})
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/oracle/billing/')
    context = {
        'client': client,
        'form': form,
    }
    return render(request, 'Oracle/Billing/AddBill.html', context)

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

def DeleteBill(request, pk):
    bill = Billing.objects.get(id=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('/oracle/billing/')
    context = {
        'bill': bill,
    }
    return render(request, 'Oracle/Billing/DeleteBill.html', context)