from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.CharField(default='describir', max_length=50)
    # imagen

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'Perfil de {self.user}'
