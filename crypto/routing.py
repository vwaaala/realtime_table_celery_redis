from django.urls import path

from crypto.consumer import CoinConsumer

ws_urlpatterns = [
    path('ws/coins/', CoinConsumer.as_asgi()),
]