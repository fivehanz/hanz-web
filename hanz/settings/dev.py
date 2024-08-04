from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False) == "True"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-b&b1#xb8s&df*ch@*w%k&3_g7vc$of2me#nf6@17jpke4@dhsr"
)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = os.environ.get("ALLOW_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DBBACKUP_STORAGE_OPTIONS["endpoint_url"] = os.environ.get("DBBACKUP_S3_ENDPOINT_URL")

try:
    from .local import *
except ImportError:
    pass
