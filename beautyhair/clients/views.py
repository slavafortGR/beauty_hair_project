from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from clients.forms import AddClientForm, ContactFormSet, AddContactForm
from clients.models import Client, Contact


def new_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        contact_formset = AddContactForm(request.POST, instance=Client())
        if form.is_valid() and contact_formset.is_valid():
            client = Client.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender']
            )

            contact = contact_formset.save(commit=True)
            contact.client = client
            contact.save()

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
    contact = get_object_or_404(Contact, pk=pk)
    context = {
        'client_info': client,
        'contact_info': contact,
        'title': 'Клиент'
    }
    return render(request, 'clients/view_client.html', context)


def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        contact_form = AddContactForm(request.POST, instance=contact)

        if form.is_valid() and contact_form.is_valid():
            form.save()
            contact_form.save()
            return redirect('clients')

    else:
        form = AddClientForm(instance=client)
        contact_form = ContactFormSet(instance=client)

        context = {
            'form': form,
            'contact_form': contact_form,
            'pk': pk,
        }
        return render(request, 'new_client.html', context)
