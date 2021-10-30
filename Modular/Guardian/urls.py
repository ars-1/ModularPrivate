from django.urls import path
from Guardian import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/',views.Login, name='login'),
    path('logout/',views.Logout,name='logout'),
]