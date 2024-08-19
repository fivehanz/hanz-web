from celery import shared_task
from django.core.management import call_command
from django.utils import timezone
import logging

# Set up logging
logger = logging.getLogger(__name__)

@shared_task
def db_backup():
    backup_time = timezone.now()

    try:
        call_command('dbbackup', '-z', '--noinput')
        message = f"Backed up successfully at {backup_time}"
        logger.info(message)
        return message
    except Exception as e:
        error_message = f"Backup failed at {backup_time}: {str(e)}"
        logger.error(error_message)
        return error_message
