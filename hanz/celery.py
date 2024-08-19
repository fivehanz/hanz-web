import os

from celery import Celery
from django.apps import apps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hanz.settings.production")

app = Celery("hanz")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: ['hanz'] + [n.name for n in apps.get_app_configs()])
