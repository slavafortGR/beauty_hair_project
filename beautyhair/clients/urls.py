from django.urls import path
from .views import clients, new_client, view_client, edit_client, delete_client, add_contact

urlpatterns = [
    path('', clients, name='clients'),
    path('<int:pk>', view_client, name='view_client'),
    path('new/', new_client, name='new_client'),
    path('edit/<int:pk>/', edit_client, name='edit_client'),
    path('add_contact/<int:pk>/', add_contact, name='add_contact'),
    path('delete/<int:pk>', delete_client, name='delete_client'),
]
