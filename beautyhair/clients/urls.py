from django.urls import path
from .views import get_clients, add_client

urlpatterns = [
    path('', add_client, name='add_client'),
    path('clients/', get_clients, name='get_clients'),
]
