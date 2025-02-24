# chat/routing.py
from django.urls import re_path

from django_base import consumers

websocket_urlpatterns = [
    re_path(r"ws/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
