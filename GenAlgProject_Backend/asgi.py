import os

from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

import django
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from experiments.routing import websocket_urlpatterns
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GenAlgProject_Backend.settings')
django.setup()
# settings.configure()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
