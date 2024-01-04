from django.http import HttpResponse
from django.shortcuts import render

def get_orders(request):
    return HttpResponse("<h1>Orders</h1>")
