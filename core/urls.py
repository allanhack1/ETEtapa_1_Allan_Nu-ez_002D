#en el core/urls se registran los metodos creados en el views
from django.urls import path
from .views import index ,galeria, form_pedido , Ver, form_mod_pedido, form_del_pedido

urlpatterns =[
    path('',index,name="index"),#el index amarillo es para llamar el metodo creado en el views
    path('galeria',galeria,name="galeria"),
    path('form_pedido',form_pedido,name="form_pedido"),
    path('ver',Ver,name="ver"),
    path('form_mod_pedido/<id>',form_mod_pedido,name="form_mod_pedido"),
    path('form_del_pedido/<id>',form_del_pedido,name="form_del_pedido"),

   
]
    







