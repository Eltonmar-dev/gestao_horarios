from django.urls import path
from . import views

app_name = "horarios"

urlpatterns = [
    path("", views.home, name="home"),
    path("criar/", views.criar_horario, name="criar"),
    path("listar/", views.listar_horarios, name="listar"),
]
