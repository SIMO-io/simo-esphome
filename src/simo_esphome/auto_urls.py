from django.urls import re_path, path

from .autocomplete_views import BoardSelectAutocomplete, PinsSelectAutocomplete
from .views import firmware_status_view, rebuild_firmware_view, wifi_update_view


urlpatterns = [
    re_path(
        'autocomplete-espboard',
        BoardSelectAutocomplete.as_view(), name='autocomplete-espboard'
    ),
    re_path(
        'autocomplete-espboard-pins',
        PinsSelectAutocomplete.as_view(), name='autocomplete-espboard-pins'
    ),
    re_path(
        r'^firmware-status/(?P<id>[0-9]+)/$', firmware_status_view,
    ),
    re_path(
        r'^rebuild-firmware/(?P<id>[0-9]+)/$', rebuild_firmware_view,
    ),
    re_path(
        r'^wifi-update/(?P<id>[0-9]+)/$', wifi_update_view,
    )
]
