from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from clients.forms import AddClientForm, ContactFormSet, AddContactForm
from clients.models import Client, Contact


def new_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        contact_formset = ContactFormSet(request.POST, instance=Client())
        if form.is_valid() and contact_formset.is_valid():
            if not any(contact_form.cleaned_data.get('contact') for contact_form in contact_formset.forms):
                form.add_error(None, 'Contact not to be empty')
            else:
                client = Client.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    gender=form.cleaned_data['gender']
                )

                contact_formset.instance = client
                contact_formset.save()

            return redirect('view_client', pk=client.pk)
        else:
            return render(request, 'clients/client_form.html',
                          {'form': form, 'contact_formset': contact_formset, 'pk': None, 'create_mode': True})
    else:
        form = AddClientForm()
        contact_formset = ContactFormSet(instance=Client())

    return render(request, 'clients/client_form.html',
                  {'form': form, 'contact_formset': contact_formset, 'pk': None, 'create_mode': True})


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
    contact = Contact.objects.filter(owner=pk)
    context = {
        'client_info': client,
        'contact_info': contact,
        'title': 'Клиент'
    }
    return render(request, 'clients/view_client.html', context)


def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    contact = get_object_or_404(Client, pk=pk)
    if request.method == 'GET':
        context = {
            'form': AddClientForm(instance=client), 'pk': pk,
            'contact_formset': ContactFormSet(instance=contact)
        }
        return render(request, 'clients/client_form.html', context)

    elif request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        contact_formset = ContactFormSet(request.POST, instance=contact)

        if form.is_valid() and contact_formset.is_valid():
            form.save()
            contact_formset.save()

            return redirect('clients')

    return render(request, 'clients/client_form.html')


def add_contact(request, pk):
    contact_formset = ContactFormSet(request.POST or None)

    if request.method == 'POST':
        if contact_formset.is_valid():
            client = get_object_or_404(Client, pk=pk)
            instances = contact_formset.save(commit=False)
            for instance in instances:
                instance.owner = client
                instance.save()
            return redirect('clients')

    return render(request, 'clients/client_form.html', {'contact_formset': contact_formset, 'pk': pk, 'add_contact_mode': True})


@require_POST
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('clients')
    else:
        return HttpResponse("Method Not Allowed", status=405)


def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('clients')
