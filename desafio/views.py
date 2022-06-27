from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

from desafio.models import Familiar

# Create your views here.

def mi_template(request):
    template1 = loader.get_template('index.html')
    
    Familiar1 = Familiar(nombre = 'Armando Barreda', edad=25, fecha_creacion='2022-06-27')
    Familiar2 = Familiar(nombre = 'Gustavo Lopez', edad=32, fecha_creacion='2022-06-27')
    Familiar3 = Familiar(nombre = 'Esteban Quito', edad=48, fecha_creacion='2022-06-27')
    Familiar1.save()
    Familiar2.save()
    Familiar3.save()
    
    render1 = template1.render({ 'familiar1': Familiar1, 'familiar2': Familiar2, 'familiar3': Familiar3})
    
    return HttpResponse(render1)
