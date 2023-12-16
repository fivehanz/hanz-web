from .base import *
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev", os.environ.get("ALLOW_HOST")]
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
