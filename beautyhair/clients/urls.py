from django.urls import path
from .views import clients, new_client, view_client, edit_client, delete_client, add_contact, delete_contact

urlpatterns = [
    path('', clients, name='clients'),
    path('<int:pk>', view_client, name='view_client'),
    path('new/', new_client, name='new_client'),
    path('<int:pk>/edit/', edit_client, name='edit_client'),
    path('<int:pk>/add_contact/', add_contact, name='add_contact'),
    path('<int:pk>/delete/', delete_contact, name='delete_contact'),
    path('<int:pk>/delete/', delete_client, name='delete_client'),
]
