from django.http import HttpResponse
from django.shortcuts import render

def get_report(request):
    return HttpResponse("<h1>Report</h1>")
