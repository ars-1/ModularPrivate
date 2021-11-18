from django.urls import include, path
from . import views

urlpatterns = [

    path('employees/employee/<int:pk>', views.EmployeeDetails),
    path('employees/', views.Employees),
    path('addEmployee/', views.AddEmployee),
    path('updateEmployee/<int:pk>', views.UpdateEmployee),
    path('deleteEmployee/<int:pk>', views.DeleteEmployee),
    path('addDesignation/', views.AddDesignation),
    path('addDepartment/', views.AddDepartment),

    path('addAttendance/', views.AddAttendance),
    path('updateAttendance/<int:pk>', views.UpdateAttendance),
    path('deleteAttendance/<int:pk>', views.DeleteAttendance),

    path('clients/', views.ClientL),
    path('billing/', views.BillingL),
    path('clients/client/<int:pk>', views.ClientDetails),
    path('addClient/', views.AddClient),
    path('updateClient/<int:pk>', views.UpdateClient),
    path('deleteClient/<int:pk>', views.DeleteClient),
    path('addBill/<int:pk>', views.AddBill),
    path('updateBill/<int:pk>', views.UpdateBill),
    path('billDetails/<int:pk>', views.BillDetails),
    path('deleteBill/<int:pk>', views.DeleteBill),

    path('tasksList/', views.Tasks),
    path('addTask/', views.addTask),
    path('updateTask/<int:pk>', views.updateTask),
    path('deleteTask/<int:pk>', views.deleteTask),
]
