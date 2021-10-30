from django.contrib import admin
from .models import Profile, Empleado, DatosIncapacidad

# Register your models here.
admin.site.register(Profile)
admin.site.register(Empleado)
admin.site.register(DatosIncapacidad)