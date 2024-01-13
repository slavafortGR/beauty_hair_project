from django.urls import path
from .views import get_clients, add_client

urlpatterns = [
    path('', get_clients, name='get_clients'),
    path('', add_client, name='add_client'),
]
