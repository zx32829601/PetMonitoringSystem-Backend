from django.urls import path

from api.consumers.notifyConsumer import NotifyConsumer
from api.consumers.chatConsumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/notify/<str:username>/', NotifyConsumer.as_asgi()),
    path('ws/chat/<str:username>/', ChatConsumer.as_asgi()),
]