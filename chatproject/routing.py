from channels.routing import ProtocolTypeRouter
from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path("chatapp/home/", consumers.PracticeConsumer.as_asgi()),
]