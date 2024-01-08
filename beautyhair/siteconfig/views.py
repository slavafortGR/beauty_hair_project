from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import SiteConfig
from .forms import SiteConfigForm
import json


json_to_model_field_mapping = {
    'type': 'gcal_type',
    'project_id': 'gcal_project_id',
    'private_key_id': 'gcal_private_key_id',
    'private_key': 'gcal_private_key',
    'client_email': 'gcal_client_email',
    'client_id': 'gcal_client_id',
    'auth_uri': 'gcal_auth_uri',
    'token_uri': 'gcal_token_uri',
    'auth_provider_x509_cert_url': 'gcal_auth_provider_x509_cert_url',
    'client_x509_cert_url': 'gcal_client_x509_cert_url',
    'universe_domain': 'gcal_universe_domain',
    'scopes': 'gcal_scopes',
}


class SiteConfigUpdateView(UpdateView):
    model = SiteConfig
    form_class = SiteConfigForm
    template_name = 'siteconfig/form_config.html'
    success_url = reverse_lazy('siteconfig:view_config')

    def get_object(self):
        return SiteConfig.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Site Configuration'
        context['include_js'] = False
        return context


def view_config(request):
    config = SiteConfig.objects.first()
    if config is None:
        return redirect('siteconfig:create_config')
    return render(request, 'siteconfig/view_config.html', {'config': config})


def create_config(request):
    if SiteConfig.objects.exists():
        return redirect('siteconfig:update_config')
    if request.method == 'POST':
        form = SiteConfigForm(request.POST, request.FILES)

        if 'json_file' in request.FILES:
            json_file = request.FILES['json_file']
            data = json.load(json_file)

            print("Загруженные данные из файла:", data)

            initial_data = {}
            for json_field, model_field in json_to_model_field_mapping.items():
                if json_field in data:
                    initial_data[model_field] = data[json_field]

            form = SiteConfigForm(initial=initial_data)

        if form.is_valid():
            form.save()
            print("Форма сохранена успешно.")
            return redirect('siteconfig:view_config')
        else:
            print("Ошибки валидации формы:", form.errors)
    else:
        form = SiteConfigForm()

    return render(request, 'siteconfig/form_config.html', {
        'form': form,
        'title': 'Create Site Configuration',
        'include_js': True,
    })
