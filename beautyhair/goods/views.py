from django.http import HttpResponse
from django.shortcuts import render

def get_goods(request):
    return HttpResponse("<h1>Goods</h1>")
