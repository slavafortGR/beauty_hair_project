from django import forms
from .models import SiteConfig


class SiteConfigForm(forms.ModelForm):
    json_file = forms.FileField(required=False, label='Google JSON File')
    main_color_scheme = forms.ChoiceField(
        choices=[('dark', 'Dark'), ('light', 'Light')],
        initial='light',
        label='Color scheme'
    )

    class Meta:
        model = SiteConfig
        fields = '__all__'
        widgets = {
            'main_begin_time': forms.Select(attrs={'type': 'time'}),
            'main_end_time': forms.TimeInput(attrs={'type': 'time'}),
            'main_color_scheme': forms.Select(),
        }
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
            'main_shop_name': 'Shop name',
            'main_color_scheme': 'Color scheme',
            'main_begin_time': 'Begin worktime',
            'main_end_time': 'End worktime',
        }

    def __init__(self, *args, **kwargs):
        super(SiteConfigForm, self).__init__(*args, **kwargs)
        self.fields['main_shop_name'].required = True
        # self.initial['main_shop_name'] = ''
        self.fields['main_color_scheme'].required = True
        self.fields['main_begin_time'].required = True
        self.fields['main_end_time'].required = True
        self.fields['main_begin_time'].widget = forms.TimeInput(attrs={'type': 'time', 'value': '00:00'}, format='%H:%M')
        self.fields['main_end_time'].widget = forms.TimeInput(attrs={'type': 'time', 'value': '00:00'}, format='%H:%M')
