from django.db import models

# Create your models here.

class Usuarios(models.Model):

    genero_eleccion = (
        ('M', 'Madculino'),
        ('F', 'Femenino'),
    )

    codigo = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(choices=genero_eleccion, max_length=100)
    estado = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_bautismo = models.DateField()

    def __str__(self):
        return self.nombre
