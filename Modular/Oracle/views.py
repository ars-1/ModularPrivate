from django.shortcuts import render, redirect
from .models import *
import datetime
from django.utils import timezone as tz
from Core.filters import *
from .forms import *
from .employeeViews import *
from .billingViews import *
from .taskViews import *

# Create your views here.

#######################################################################################################################
###############################################  Employees Section   ##################################################
#######################################################################################################################