from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_nac=models.DateField()
    correo_elec=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=10)
    direccion=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
