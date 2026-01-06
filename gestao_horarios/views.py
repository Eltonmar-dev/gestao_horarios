from django.shortcuts import render, redirect
from .models import Horario

def home(request):
    return render(request, 'horarios/home.html')

def criar_horario(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')
        dia = request.POST.get('dia')
        if titulo and inicio and fim and dia:
            Horario.objects.create(titulo=titulo, inicio=inicio, fim=fim, dia=dia)
            return redirect('home')
    return render(request, 'horarios/criar_horario.html')
