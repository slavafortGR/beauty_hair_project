from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from clients.forms import AddClientForm, ContactFormSet, AddContactForm
from clients.models import Client, Contact


def new_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        contact_formset = ContactFormSet(request.POST, instance=Client())
        if form.is_valid() and contact_formset.is_valid():
            client = Client.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender']
            )

            contact_formset.instance = client
            contact_formset.save()

            return redirect('view_client', pk=client.pk)
        else:
            return HttpResponse("Invalid data", status=400)
    else:
        form = AddClientForm()
        contact_formset = ContactFormSet(instance=Client())

    return render(request, 'clients/new_client.html', {'form': form, 'contact_formset': contact_formset})


def clients(request):
    all_clients = Client.objects.all()
    all_contacts = Contact.objects.all()
    context = {
        'clients': all_clients,
        'contacts': all_contacts,
        'title': 'Клиенты'
    }
    return render(request, 'clients/clients.html', context)


def view_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    contact = Contact.objects.get(owner=pk)
    context = {
        'client_info': client,
        'contact_info': contact,
        'title': 'Клиент'
    }
    return render(request, 'clients/view_client.html', context)


def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    contact = Contact.objects.get(owner=pk)

    if request.method == 'GET':
        context = {
            'form': AddClientForm(instance=client), 'pk': pk,
            'contact_formset': AddContactForm(instance=contact)
        }
        return render(request, 'clients/new_client.html', context)

    elif request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        contact_formset = AddContactForm(request.POST, instance=contact)

        if form.is_valid() and contact_formset.is_valid():
            form.save()
            contact_formset.save()

            return redirect('clients')

    return render(request, 'clients/new_client.html')


def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('clients')
