from django.shortcuts import render,redirect    
from .models import Pedido #se trabaja con una sola clase
from .forms import PedidoForm
#from django.shortcuts import render, redirect, get_object_or_404
#from . models import index, Genre


 
def index(request):
    return render(request,'index.html',)


def galeria(request):
    encargo=Pedido.objects.all()#muestra todos los atributos de la clase Pedido
    return render(request,'galeria.html',context={'datos':encargo},)


def form_pedido(request):# metodo trabaja con forms.py y form_crearpedido

    if request.method=='POST': 
        pedido_forms =  PedidoForm(request.POST)
        if pedido_forms.is_valid():
            pedido_forms.save()#save reemplaza el insert 
            return redirect('galeria')
    else:
        pedido_forms= PedidoForm()
    return render(request,'core/form_crearpedido.html',{'pedido_forms':pedido_forms})


def Ver(request):
    pedido = Pedido.objects.all()

    return render(request, 'core/ver.html', context={'pedido':pedido})

def form_mod_pedido(request,id):
    pedido = Pedido.objects.get(RutCliente=id)

    datos ={
        'form': PedidoForm(instance=pedido)
    }
    if request.method == 'POST': 
        formulario = PedidoForm(data=request.POST, instance = pedido)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('ver')
    return render(request, 'core/form_mod_pedido.html', datos)




def form_del_pedido(request,id):
    pedido = Pedido.objects.get(RutCliente=id)
    pedido.delete()
    return redirect('ver')





