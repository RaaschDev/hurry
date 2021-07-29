from django.db import models
from django.views.generic.list import ListView
from .models import Evento


class EventoList(ListView):
    model = Evento
    template_name = 'eventos/eventos_list.html'
    