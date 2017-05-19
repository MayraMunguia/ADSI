from django.db import models
from django.utils import timezone

class Mensaje(models.Model):
    Nombre = models.TextField(null=True)
    Correo = models.CharField(max_length=50, null=True)
    Mensaje = models.TextField(null=True)
        
        

    def publish(self):
        self.save()
