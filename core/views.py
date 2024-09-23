from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def suporte(request):
    return render(request,'suporte.html')

def contato(request):
    return render(request,'contato.html')

def eletro(request):
    return render(request,'eletro.html')

def monitor(request):
    return render(request,'monitor.html')

def medidor(request):
    return render(request,'medidor.html')