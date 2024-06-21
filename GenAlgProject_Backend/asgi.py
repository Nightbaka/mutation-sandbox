import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from experiments.routing import websocket_urlpatterns

# Set the environment variable before any Django imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GenAlgProject_Backend.settings')

# Setup Django
django.setup()

# Now import the ASGI application
from django.core.asgi import get_asgi_application

# Get the Django ASGI application
django_asgi_app = get_asgi_application()

# Define the ASGI application
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
