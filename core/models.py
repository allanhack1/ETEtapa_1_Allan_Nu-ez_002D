from django.db import models
from django.db.models.fields import CharField
#especificacion de las clases
# Create your models here.

class Delivery(models.Model):
    IdDelivery=models.IntegerField(primary_key=True,verbose_name='Id de delivery')
    NombreServicio=models.CharField(max_length=30, verbose_name='Nombre del servicio')

    def __str__(self):
        return(self.NombreServicio)

class Pedido(models.Model):
    RutCliente=models.CharField(max_length=10,primary_key=True,verbose_name='RutCliente')
    #Nombre=models.CharField(max_length=70,verbose_name='Nombre')
    NumeroIdenticacion=models.CharField(max_length=25,verbose_name='NumeroIdenticacion')
    Nombre=models.CharField(max_length=40,verbose_name='Nombre')
    Dirección=models.CharField(max_length=40,verbose_name='Dirección')
    Telefono=models.CharField(max_length=40,verbose_name='Telefono')
   

    def __str__(self):
        return(self.RutCliente)



