from django.urls import re_path
from experiments import consumers

websocket_urlpatterns = [
    # re_path(r'ws/experiment/$', consumers.ExperimentConsumer.as_asgi()),
    re_path(r'ws/history/$', consumers.HistoryConsumer.as_asgi())
]