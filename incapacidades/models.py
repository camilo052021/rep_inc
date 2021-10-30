
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


t_documentos= [
    ('CC', 'Cédula Ciudadanía'),
    ('PP', 'Permiso Permanente'),
    ('CE', 'Cédula Extranjería'),
    ('TI', 'Tarjeta de identidad'),
    ]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.CharField(default='describir', max_length=50)
    # imagen

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'Perfil de {self.user}'


class Empleado(models.Model):
    cedula = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Documento")
    tipo_doc = models.CharField(verbose_name="Tipo Documento", max_length=200, choices=t_documentos)
    telefono = models.CharField(verbose_name="Telefono", max_length=10)
    cargo = models.CharField(verbose_name="Cargo", max_length=255)
    area = models.CharField(verbose_name="Area", max_length=255)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'Número de ´Documento {self.cedula}'


class DatosIncapacidad(models.Model):
    cedula = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Documento")
    eps = models.CharField(verbose_name="EPS", max_length=100)
    origen = models.CharField(verbose_name="Descripción Enfermedad", max_length=255)
    fecha_inicio = models.DateField(verbose_name="Fecha Inicio incapacidad")
    fecha_fin = models.DateField(verbose_name="Fecha Fin incapacidad")
    dias_incapacidad = models.IntegerField(verbose_name="Días de Incapacidad")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    archivo_inc = models.FileField(default='/media/archivos', verbose_name="Cargue el archivo con la incapacidad")


    class Meta:
        verbose_name = 'Incapacidad'
        verbose_name_plural = 'Incapacidades'

    def __str__(self):
        return f'Número de ´Documento {self.cedula}'

