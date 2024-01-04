from django.http import HttpResponse
from django.shortcuts import render

def get_clients(request):
    return HttpResponse("<h1>Clients</h1>")
