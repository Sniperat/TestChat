from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'chat/(?P<room_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'videochat/(?P<room_id>\w+)/$', consumers.VideoChatConsumer.as_asgi()),

]
