import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from Familia.models import Familiar
# Create your views here.

def show_home(request):
    familiar1 = Familiar(nombre = "Marcelo", edad = 37,  nacimiento = "1985-03-26")
    familiar2 = Familiar(nombre = "Dario", edad = 39,  nacimiento = "1983-05-13")
    familiar3 = Familiar(nombre = "Juliana", edad = 32,  nacimiento = "1991-09-20")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    context = {"familiar1": familiar1, "familiar2": familiar2, "familiar3": familiar3}
    return render(request, "Familia/familiar1.html", context)
 