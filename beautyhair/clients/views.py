from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from clients.forms import AddClientForm
from clients.models import Client


def new_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = Client.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender']
            )
            return redirect('view_client', pk=client.pk)
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        form = AddClientForm()

    return render(request, 'clients/new_client.html', {'form': form})


def clients(request):
    all_clients = Client.objects.all()
    context = {
        'clients': all_clients,
        'title': 'Клиенты'
    }
    return render(request, 'clients/clients.html', context)


def view_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/view_client.html', {'client': client})
