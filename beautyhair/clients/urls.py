from django.urls import path
from .views import clients, new_client, view_client, edit_client

urlpatterns = [
    path('', clients, name='clients'),
    path('<int:pk>', view_client, name='view_client'),
    path('new/', new_client, name='new_client'),
    path('<int:pk>', edit_client, name='edit_client')
]
