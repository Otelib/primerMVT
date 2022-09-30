from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def show_home(request):
    return render(request, "Familia/familiar1.html")
