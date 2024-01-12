from django.shortcuts import render, redirect

from clients.forms import AddClient
from clients.models import Client


def get_clients(request):
    if request.method == 'POST':
        form = AddClient(request.POST)
        if form.is_valid():
            try:
                Client.objects.create(**form.cleaned_data)
                return redirect('get_clients')
            except:
                form.add_error('', 'Error')
    else:
        form = AddClient()
    return render(request, 'clients/get_clients.html', {'form': form, 'title': 'Создать клиента'})
