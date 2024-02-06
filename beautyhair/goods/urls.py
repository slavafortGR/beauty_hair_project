from django.urls import path
from .views import get_goods

urlpatterns = [
    path('', get_goods, name='goods')
]
