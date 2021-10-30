from django.urls import path

#from rid.incapacidades import views
from .views import home

urlpatterns = [
    path('', home, name='home')
]