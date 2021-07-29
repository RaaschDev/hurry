from django import forms
from .models import Evento, Artista

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ("nome","data","inicio", "final","endereco","endereco2","cep","gestor")


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ("nome","inicio","final","foto","valor","evento")


