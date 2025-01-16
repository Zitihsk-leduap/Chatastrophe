"""
ASGI config for Chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')

django_asgi_app = get_asgi_application()

from rt_chat import routing
application = ProtocolTypeRouter(
  {
  'http':django_asgi_app,
  'websocket':AllowedHostsOriginValidator(
    AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
  ),

  }
)
