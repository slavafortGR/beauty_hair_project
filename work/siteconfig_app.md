### `siteconfig` app

#### Abstract:

`siteconfig` app is used to store site-wide configuration parameters. It's a singleton model, so there's only one instance of it in the database. It holds and operates parameters for Google Calendar API and other app parameters.

`webcalendar_service_account.json` structure:

```json
{
  "type": "service_account",
  "project_id": "webcalendar-11223344",
  "private_key_id": "af7c1d428b6878c93093954ecd4935c6",
  "private_key": "-----BEGIN PRIVATE KEY-----\n5e9246b2a3f1061\n-----END PRIVATE KEY-----\n",
  "client_email": "web-calendar@webcalendar-11223344.iam.gserviceaccount.com",
  "client_id": "297484005579487298",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/webcalendar-11223344.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com",
  "scopes": "https://www.googleapis.com/auth/calendar"
}
```

#### Note:

* `scopes` parameter wasn't in generic json file, it was added by hand, but it's mandatory for working with Google Calendar API.
* Fields' naming in `SiteConfig` model:
  * `gcal_*` - Google Calendar API parameters
  * `main_*` - other app parameters
-----

#### Errata:

There's an unholy fucking mess with some `input` fields in `siteconfig/templates/siteconfig/form_config.html` (see comments in the file, lines 49-51).
There's a workaround for this, but I left it for future fix (maybe).

**Possible fix (in forms.py):**

```python
from django import forms
from .models import SiteConfig

class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfig
        fields = '__all__'
        widgets = {
            'gcal_type': forms.TextInput(attrs={'class': 'input is-fullwidth'}),
            'gcal_project_id': forms.TextInput(attrs={'class': 'input is-fullwidth'}),
            'gcal_private_key_id': forms.TextInput(attrs={'class': 'input is-fullwidth'}),
            # ... and so on for other fields
        }
        labels = {
            'gcal_type': 'Type',
            'gcal_project_id': 'Project ID',
            # ... and so on for other fields
        }

    # Initializing the form to set initial values
    def __init__(self, *args, **kwargs):
        super(SiteConfigForm, self).__init__(*args, **kwargs)
        # You can set initial values or change  CSS attributes here
        self.fields['main_begin_time'].widget.attrs.update({'class': 'input is-fullwidth'})
        self.fields['main_end_time'].widget.attrs.update({'class': 'input is-fullwidth'})
        # ... and so on for other fields, if necessary

```
