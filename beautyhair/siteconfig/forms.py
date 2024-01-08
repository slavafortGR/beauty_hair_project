from django import forms
from .models import SiteConfig


class SiteConfigForm(forms.ModelForm):
    json_file = forms.FileField(required=False, label='Google JSON File')

    class Meta:
        model = SiteConfig
        fields = '__all__'
        labels = {
            'gcal_type': 'Type',
            'gcal_project_id': 'Project ID',
            'gcal_private_key_id': 'Private Key ID',
            'gcal_private_key': 'Private Key',
            'gcal_client_email': 'Client Email',
            'gcal_client_id': 'Client ID',
            'gcal_auth_uri': 'Auth URI',
            'gcal_token_uri': 'Token URI',
            'gcal_auth_provider_x509_cert_url': 'Auth Provider X509 Cert URL',
            'gcal_client_x509_cert_url': 'Client X509 Cert URL',
            'gcal_universe_domain': 'Universe Domain',
            'gcal_scopes': 'Scopes',
            'main_shop_name': 'Shop Name',
            'main_color_scheme': 'Color Scheme',
            'main_begin_time': 'Begin Time',
            'main_end_time': 'End Time',
        }

    def __init__(self, *args, **kwargs):
        super(SiteConfigForm, self).__init__(*args, **kwargs)
        self.fields['main_shop_name'].required = False
        self.fields['main_color_scheme'].required = False
        self.fields['main_begin_time'].required = False
        self.fields['main_end_time'].required = False

    def clean(self):
        cleaned_data = super().clean()
        json_file = cleaned_data.get('json_file')

        # Пропуск валидации полей, если загружен файл
        if json_file:
            for field_name in self.fields:
                if field_name.startswith('gcal_'):
                    self.fields[field_name].required = False
        return cleaned_data
