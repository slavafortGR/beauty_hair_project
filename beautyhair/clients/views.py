from django.shortcuts import render, redirect

from clients.forms import AddClient
from clients.models import Client


def add_client(request):
    if request.method == 'POST':
        form = AddClient(request.POST)
        if form.is_valid():
            try:
                Client.objects.create(**form.cleaned_data)
                return redirect('get_clients')
            except:
                form.add_error('', 'Error')
                print(form.cleaned_data)
    else:
        form = AddClient()
    return render(request, 'clients/add_client.html', {'form': form, 'title': 'Создать клиента'})


def get_clients(request):
    all_clients = Client.objects.all()
    context = {'all_clients': all_clients}
    return render(request, 'clients/get_clients.html', context, {'title': 'Клиенты'})
