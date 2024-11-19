from django.db import models

class Productos(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=20)
    nombre=models.CharField(max_length=6)
    marca=models.CharField(max_length=6)
    tipo=models.CharField(max_length=6)
    volumen=models.IntegerField(max_length=6)
    precio=models.DecimalField(max_length=6)
    
    def_str_(self)
# Create your models here.
