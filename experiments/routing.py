from django.urls import re_path
from experiments import consumers

websocket_urlpatterns = [
    re_path(r'ws/experiment/$', consumers.MyConsumer.as_asgi()),
]