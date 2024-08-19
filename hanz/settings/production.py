from .base import *
import os

SECRET_KEY = os.environ.get("SECRET_KEY")

# wagtail frontend cache (cloudflare), invalidated on change
WAGTAILFRONTENDCACHE = {
    'cloudflare': {
        'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudflareBackend',
        'BEARER_TOKEN': os.environ.get("CLOUDFLARE_BEARER_TOKEN", ""),
        'ZONEID': os.environ.get("CLOUDFLARE_ZONEID", ""),
    },
}

ALLOWED_HOSTS = os.environ.get("ALLOW_HOSTS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")

try:
    from .local import *
except ImportError:
    pass
