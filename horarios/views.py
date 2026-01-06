from django.shortcuts import render, redirect
from .forms import HorarioForm
from .models import Horario

def home(request):
    total = Horario.objects.count()
    return render(request, "horarios/home.html", {"total": total})


def criar_horario(request):
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("horarios:listar")
    else:
        form = HorarioForm()

    return render(request, "horarios/criar_horario.html", {"form": form})


def listar_horarios(request):
    horarios = Horario.objects.all().order_by("dia", "inicio")
    return render(request, "horarios/listar_horarios.html", {"horarios": horarios})

