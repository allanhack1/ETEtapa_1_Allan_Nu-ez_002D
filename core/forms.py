from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta: #define elementos
        model=Pedido
        fields=['RutCliente','NumeroIdenticacion','Nombre','Dirección','Telefono']
        labels ={
            'RutCliente': 'Ingrese su rut', 
            'NumeroIdenticacion': 'Ingrese Numero de Identicacion', 
            'Nombre': 'Ingrese Nombre', 
            'Dirección': 'Ingrese su dirección',
            'Telefono': 'Ingrese su Telefono',
            
        }


        widgets={
            'RutCliente': forms.TextInput(
                attrs={#atributos
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su rut', 
                    'id': 'rut'
                }
            ), 
            'NumeroIdenticacion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su NumeroIdenticacion', 
                    'id': 'NumeroIdenticacion'
                }
            ), 
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Nombre', 
                    'id': 'Nombre'
                }
            ), 
            'Dirección': forms.TextInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'Ingrese su dirección', 
                    'id': 'dirección',
                    #'style':'width: 350px',
                    #'class':'centrado'
                    
                }
            ), 
             'Telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Telefono', 
                    'id': 'Telefono'
                }
            ), 
            

        }


        
