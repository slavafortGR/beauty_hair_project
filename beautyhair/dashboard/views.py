from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Beauty Hair main page</h1>")
