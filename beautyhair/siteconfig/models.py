from django.db import models


class SiteConfig(models.Model):
    gcal_type = models.CharField(max_length=128, null=False, blank=False)
    gcal_project_id = models.CharField(max_length=256, null=False, blank=False)
    gcal_private_key_id = models.CharField(max_length=1024, null=False, blank=False)
    gcal_private_key = models.TextField(null=False, blank=False)
    gcal_client_email = models.EmailField(null=False, blank=False)
    gcal_client_id = models.CharField(max_length=256, null=False, blank=False)
    gcal_auth_uri = models.URLField(null=False, blank=False)
    gcal_token_uri = models.URLField(null=False, blank=False)
    gcal_auth_provider_x509_cert_url = models.URLField(null=False, blank=False)
    gcal_client_x509_cert_url = models.URLField(null=False, blank=False)
    gcal_universe_domain = models.CharField(max_length=128, null=False, blank=False)
    gcal_scopes = models.URLField(null=False, blank=False)

    main_shop_name = models.CharField(max_length=128, null=False, blank=True)
    main_color_scheme = models.CharField(max_length=128, null=False, blank=True)
    main_begin_time = models.TimeField(null=False, blank=True)
    main_end_time = models.TimeField(null=False, blank=True)

    class Meta:
        db_table = 'siteconfig'

    def save(self, *args, **kwargs):
        if not self.pk and SiteConfig.objects.exists():
            return
        return super(SiteConfig, self).save(*args, **kwargs)
