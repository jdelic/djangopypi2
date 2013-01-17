# -* encoding: utf-8 *-

from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.backends import RemoteUserBackend


class ProxyRemoteUserMiddleware(RemoteUserMiddleware):
    """
    This authenticates the remote user against the commonly
    used HTTP_REMOTE_USER meta field so that HTTP AUTH
    authentication actually works with gunicorn.
    """
    header = "HTTP_REMOTE_USER"


class ProxyRemoteUserBackend(RemoteUserBackend):
    """
    This makes sure unknown users don't gain access.
    """
    create_unknown_user = False
