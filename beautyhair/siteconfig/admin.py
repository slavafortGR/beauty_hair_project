# from django.contrib import admin
# from .models import SiteConfig
#
#
# @admin.register(SiteConfig)
# class SiteConfigAdmin(admin.ModelAdmin):
#     list_display = ['project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'auth_uri', 'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url', 'universe_domain', 'scopes']
#     list_filter = ['project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'auth_uri', 'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url', 'universe_domain', 'scopes']
#     search_fields = ['project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'auth_uri', 'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url', 'universe_domain', 'scopes']
#     ordering = ['project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'auth_uri', 'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url', 'universe_domain', 'scopes']
#     readonly_fields = ['project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'auth_uri', 'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url', 'universe_domain', 'scopes']
#     fieldsets = [
#         ('Project ID', {'fields': ['project_id']}),
#         ('Private Key ID', {'fields': ['private_key_id']}),
#         ('Private Key', {'fields': ['private_key']}),
#         ('Client Email', {'fields': ['client_email']}),
#         ('Client ID', {'fields': ['client_id']}),
#         ('Auth URI', {'fields': ['auth_uri']}),
#         ('Token URI', {'fields': ['token_uri']}),
#         ('Auth Provider X509 Cert URL', {'fields': ['auth_provider_x509_cert_url']}),
#         ('Client X509 Cert URL', {'fields': ['client_x509_cert_url']}),
#         ('Universe Domain', {'fields': ['universe_domain']}),
#         ('Scopes', {'fields': ['scopes']}),
#     ]
