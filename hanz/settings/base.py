"""
Django settings for hanz project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django.conf.global_settings import STORAGES

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DEBUG = os.environ.get("DEBUG", False)
WAGTAIL_CACHE = os.environ.get("WAGTAIL_CACHE", not DEBUG)

# wagtail frontend cache (cloudflare), invalidated on change
WAGTAILFRONTENDCACHE = {
    'cloudflare': {
            'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudflareBackend',
            'BEARER_TOKEN': os.environ.get("CLOUDFLARE_BEARER_TOKEN", ""),
            'ZONEID': os.environ.get("CLOUDFLARE_ZONEID", ""),
        },
}

# Application definition

INSTALLED_APPS = [
    "base",
    "blog",
    "project",
    "home",
    "search",
    "wagtail_ai",
    "wagtailseo",
    "wagtailcache",
    "wagtail.contrib.settings",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.frontend_cache",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django_celery_beat",
    "compressor",
    "crispy_forms",
    "crispy_tailwind",
    "dbbackup",  # django-dbbackup
    "storages",  # django-storages
    # TODO: wagtail-storages for documents does not work at the moment
    # "wagtail_storages.apps.WagtailStoragesConfig",
]

MIDDLEWARE = [
    "wagtailcache.cache.UpdateCacheMiddleware",  # wagtail cache
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "wagtailcache.cache.FetchFromCacheMiddleware",  # wagtail cache
]

ROOT_URLCONF = "hanz.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "hanz.wsgi.application"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# django-dbbackup settings
DBBACKUP_STORAGE = "storages.backends.s3.S3Storage"

DBBACKUP_STORAGE_OPTIONS = {
    "access_key": os.environ.get("DBBACKUP_S3_ACCESS_KEY_ID"),
    "secret_key": os.environ.get("DBBACKUP_S3_SECRET_KEY"),
    "bucket_name": os.environ.get("DBBACKUP_S3_BUCKET_NAME"),
    'endpoint_url': os.environ.get("DBBACKUP_S3_ENDPOINT_URL"),
    "region_name": os.environ.get("DBBACKUP_S3_REGION_NAME", "us-east-1"),
    "default_acl": "private",
}

AWS_S3_ADDRESSING_STYLE = os.environ.get("S3_ADDRESSING_STYLE", "path")
# AWS_S3_SIGNATURE_VERSION = "s3v4"

# CACHE
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/1"),
        "TIMEOUT": 60 * 60 * 24 * 7,  # 1 week
    }
}

# Email
EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
ANYMAIL = {
    "RESEND_API_KEY": os.environ.get("RESEND_API_KEY"),
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_HOST = os.environ.get("DJANGO_STATIC_HOST", "")
STATIC_URL = STATIC_HOST + "/static/"


# Storage Backends
STORAGES["default"] = {
    "BACKEND": "storages.backends.s3.S3Storage",
    "OPTIONS": {
        "access_key": os.environ.get("MEDIA_S3_ACCESS_KEY_ID"),
        "secret_key": os.environ.get("MEDIA_S3_SECRET_KEY"),
        "bucket_name": os.environ.get("MEDIA_S3_BUCKET_NAME"),
        "region_name": os.environ.get("MEDIA_S3_REGION_NAME", "us-east-1"),
        "endpoint_url": os.environ.get("MEDIA_S3_ENDPOINT_URL"),
        "use_ssl": os.environ.get("MEDIA_S3_USE_SSL", True) == "True",
        "addressing_style": "path",
        "default_acl": "private",
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

WAGTAIL_STORAGES_DOCUMENT_HOOK_ORDER = 900

# Static Files
# Boolean that decides if compression will happen.
COMPRESS_ENABLED: bool = os.environ.get("COMPRESS_ENABLED", not DEBUG) == "True"
COMPRESS_STORAGE = (
    "compressor.storage.GzipCompressorFileStorage"  # gzip compression for static files
)

# Boolean that decides if compression should be done outside of the request/response loop.
# Must enable this to use with Whitenoise
COMPRESS_OFFLINE: bool = os.environ.get("COMPRESS_OFFLINE", False) == "True"
# COMPRESS_OFFLINE = True

COMPRESS_ROOT = os.path.join(BASE_DIR, "static")

# Wagtail settings
WAGTAIL_SITE_NAME = "hanz"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "https://hanz.jsmx.org"

# wagtail ai
WAGTAIL_AI = {
    "BACKENDS": {
        "default": {
            "CLASS": "wagtail_ai.ai.llm.LLMBackend",
            "CONFIG": {
                "MODEL_ID": "mistralai/Mistral-7B-Instruct-v0.1",
                "TOKEN_LIMIT": 4096,
                "INIT_KWARGS": {
                    "key": os.environ.get(
                        "LLM_ANYSCALE_ENDPOINTS_KEY",
                        "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    )
                },
            },
        }
    }
}

# crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379/1"
)
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
