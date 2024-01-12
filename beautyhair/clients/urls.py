from django.urls import path
from .views import get_clients


urlpatterns = [
    path('', get_clients, name='get_clients')
]
