import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# celery instance
app = Celery('core')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coin_stats_30s': {
        'task': 'crypto.tasks.get_coin_stats',
        'schedule': 10.0
    }
}

app.autodiscover_tasks()