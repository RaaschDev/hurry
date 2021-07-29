from django.urls import path
from .views import EventoList
urlpatterns = [
    path('', EventoList.as_view(), name='eventos'),
]