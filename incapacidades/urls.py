from django.urls import path

#from rid.incapacidades import views
from .views import home, register

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
]