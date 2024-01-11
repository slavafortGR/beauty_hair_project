from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, resolve
from django.views.generic import UpdateView
from .models import SiteConfig
from .forms import SiteConfigForm
import json


json_to_model_fields_mapping = {
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

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object():
            return redirect('siteconfig:view_config')
        return super(SiteConfigUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        siteconf = SiteConfig.objects.first()
        if siteconf is None:
            return None
        return siteconf

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Site Configuration'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Настройки успешно обновлены.")
        return response


def view_config(request):
    config = SiteConfig.objects.first()
    warning_message = ''
    gcal_fields_filled = all(getattr(config, field, None) for field in json_to_model_fields_mapping.values())

    current_url_name = resolve(request.path_info).url_name
    show_json_upload = config is None or current_url_name == 'update_config'

    if config is None or not gcal_fields_filled:
        warning_message = "Все поля обязательны и должны быть заполнены. До этих пор приложение неработоспособно."

    return render(request, 'siteconfig/view_config.html', {
        'config': config,
        'warning_message': warning_message,
        'show_json_upload': show_json_upload,
    })


def upload_json(request):
    if request.method == 'POST' and 'json_file' in request.FILES:
        json_file = request.FILES['json_file']
        try:
            data = json.load(json_file)
            request.session['gcal_data'] = data
            messages.success(request, "Файл JSON успешно загружен.")
            return redirect('siteconfig:create_config')
        except json.JSONDecodeError:
            messages.error(request, "Ошибка в формате файла JSON.")
    return redirect('siteconfig:view_config')


def create_config(request):
    if SiteConfig.objects.exists():
        return redirect('siteconfig:update_config')

    initial_data = {}
    if 'gcal_data' in request.session:
        json_data = request.session['gcal_data']
        for json_field, model_field in json_to_model_fields_mapping.items():
            if json_field in json_data:
                initial_data[model_field] = json_data[json_field]

    if request.method == 'POST':
        form = SiteConfigForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session.pop('gcal_data', None)
            messages.success(request, "Настройки успешно сохранены.")
            return redirect('siteconfig:view_config')
        else:
            print("Ошибки валидации формы:", form.errors)
    else:
        form = SiteConfigForm(initial=initial_data)

    return render(request, 'siteconfig/form_config.html', {
        'form': form,
        'title': 'Create Site Configuration',
    })
