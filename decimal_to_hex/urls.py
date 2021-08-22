from django.urls import path
from decimal_to_hex.api import DecToHexView

urlpatterns = [
    path('', DecToHexView.as_view(), name="decimal_to_hex"),
]
