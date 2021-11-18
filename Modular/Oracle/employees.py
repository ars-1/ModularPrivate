from django.db import models
import datetime
from django.contrib.auth.models import User

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


# Designations
class Designation(models.Model):
    title = models.CharField(max_length=100, null=True)
    datestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# Department
class Department(models.Model):
    title = models.CharField(max_length=100, null=True)
    datestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


# Employee Model
class Employee(models.Model):

    # Personnal Info:
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, null=True, blank=True, default="None")
    lname = models.CharField(max_length=100, null=True, blank=True, default="None")
    mobile = models.CharField(max_length=100, null=True, blank=True, default="None")
    dob = models.DateField(null=True, blank=True, default=datetime.datetime.now)
    cnic = models.CharField(default=00000-0000000-0, max_length=16)
    housestreet = models.CharField(max_length=100, null=True, blank=True, default="None")
    city = models.CharField(max_length=100, null=True, blank=True, default="None")
    country = models.CharField(max_length=100, null=True, blank=True, default="None")

    # For Comapny:
    profile_pic = models.ImageField(upload_to="profiles", null=True, blank=True, default="fault.jpg")
    salary = models.IntegerField(null=True, blank=True, default=0)
    email = models.CharField(max_length=100, null=True, blank=True, default="None")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    designation = models.ManyToManyField(Designation, blank=True)
    joining = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return u"%s %s"%(self.fname, self.lname)


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################




#Attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    Statuschoices = (
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Half Time", "Half Time"),
        ("Leave", "Leave"),
    )
    status = models.CharField(max_length=100, choices=Statuschoices, null=True)
    datestamp = models.DateTimeField(default=datetime.datetime.now(), null=True)
    monthChoice = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month = models.CharField(default=datetime.datetime.today().strftime("%B"), choices=monthChoice, max_length=100, null=True)

    def __str__(self):
        return u"%s %s %s" %(self.employee, self.status, self.datestamp)

######################################################################################################################
######################################################################################################################
######################################################################################################################