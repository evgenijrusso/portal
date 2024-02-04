import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work.settings')

app = Celery('work')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

#  -------------------  расписание задач ----------------------
app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'news.tasks.hello',
        'schedule': 15,
    },
}

app.conf.beat_schedule = {
    'create_new_post_at_once': {
        'task': 'news.tasks.send_newsletter',
        'schedule': crontab(),
    },
}

app.conf.beat_schedule = {
    'action_every_monday8am': {
        'task': 'news.tasks.send_mail_every_monday8am',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': ()
    }
}

app.conf.timezone = 'UTC'

# celery -A work worker -l INFO --pool=solo
# celery -A work beat -l INFO
#  celery -A work purge  -  удаление задачи