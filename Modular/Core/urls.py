from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Dashboard),
    path('oracle/', include('Oracle.urls')),
    path('guardian/', include('Guardian.urls')),
]