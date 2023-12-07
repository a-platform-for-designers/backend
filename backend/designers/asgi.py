import os
import django
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'designers.settings')
django.setup()

from .tokenauth_middleware import TokenAuthMiddleware  # noqa: E402
from api import chat_routing  # noqa: E402

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        TokenAuthMiddleware(URLRouter(chat_routing.websocket_urlpatterns))
    )
})
