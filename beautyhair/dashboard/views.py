from django.shortcuts import render


def index(request):
    return render(request, "dashboard/list.html", {"title": "Главная страница"})
