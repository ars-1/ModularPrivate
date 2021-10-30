from django.db import models
import datetime
from .employees import *


# Billing

class Package(models.Model):
    title = models.CharField(max_length=100, null=True)
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    # Personal
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to="clients", null=True, default="clients/linuxghost.jpg")
    mobile = models.CharField(max_length=100, null=True)
    cnic = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    # Company
    username = models.CharField(max_length=100, null=True, unique=True)
    password = models.CharField(max_length=100, null=True)
    package = models.ForeignKey(Package, null=True, on_delete=models.CASCADE)
    bill = models.IntegerField(null=True, unique=True)
    wire = models.BooleanField(default=True)
    router = models.BooleanField(default=True)
    reference = models.CharField(max_length=200, null=True)
    due = models.IntegerField(null=True)
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Billing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, to_field='username', related_name='user')
    billA = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, blank=True)
    datestamp = models.DateTimeField(null=True, default=datetime.datetime.now())
    def __str__(self):
        return self.client.username
