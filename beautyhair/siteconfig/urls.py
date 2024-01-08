from django.urls import path
from .views import view_config, create_config, SiteConfigUpdateView

app_name = 'siteconfig'

urlpatterns = [
    path('', view_config, name='view_config'),
    path('update/', SiteConfigUpdateView.as_view(), name='update_config'),
    path('create/', create_config, name='create_config'),
]
