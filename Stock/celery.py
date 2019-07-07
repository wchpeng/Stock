from __future__ import absolute_import, unicode_literals
import os
import time
from celery import Celery, shared_task
from celery.schedules import crontab
from django.core import management

# set the default Django settings module for the 'celery' program.
env = os.environ.get("PY3_DJANGO2_SETTING_ENV", "develop")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Stock.%s' % env)

app = Celery('Stock')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    time.sleep(5)
    print('Request: {0!r}'.format(self.request))


@shared_task
def ttt():
    print("start ttt sleep(10) _______")
    time.sleep(10)
    print("end ttt____________________")
    return "yyyyyyyyyyyyyyyyyyyyyy"


@shared_task
def sync_data_to_stock():
    management.call_command('sync_data_to_stock')


@shared_task
def sync_data_to_stock_history():
    management.call_command('sync_data_to_stock_history')


app.conf.beat_schedule = {
    'update_latest_stock_info_every_mon2fri0': {
        'task': 'Stock.celery.ttt',
        # 'schedule': crontab(day_of_week={1, 2, 3, 4, 5}),
        # 'schedule': crontab('*'),
        'schedule': 20,
        'args': ()
    },
    # 周一至周五，每天的 11.30, 15:00 执行一次往历史库插入数据的操作
    'add_stock_history_info_1130': {
        'task': 'Stock.celery.sync_data_to_stock_history_mon2fri',
        'schedule': crontab(minute=30, hour=11, day_of_week={1, 2, 3, 4, 5}),
        'args': ()
    },
    'add_stock_history_info_1500': {
        'task': 'Stock.celery.sync_data_to_stock_history_mon2fri',
        'schedule': crontab(minute=0, hour=15, day_of_week={1, 2, 3, 4, 5}),
        'args': ()
    },

    # 周一周五，每天的 9:30-11:30, 13:00-15:00 这期间，每十分钟更新一次 stock 表实时信息
    'update_latest_stock_info_every_mon2fri_09': {
        'task': 'Stock.celery.sync_data_to_stock',
        'schedule': crontab(minute=[40, 50], hour=9, day_of_month={1, 2, 3, 4, 5}),
        'args': ()
    },
    'update_latest_stock_info_every_mon2fri_11': {
        'task': 'Stock.celery.sync_data_to_stock',
        'schedule': crontab(minute={0, 10, 20, 30}, hour=11, day_of_month={1, 2, 3, 4, 5}),
        'args': ()
    },
    'update_latest_stock_info_every_mon2fri_10_11_13_14': {
        'task': 'Stock.celery.sync_data_to_stock',
        'schedule': crontab(minute='*/10', hour={10, 13, 14}, day_of_month={1, 2, 3, 4, 5}),
        'args': ()
    },
    'update_latest_stock_info_every_mon2fri_15': {
        'task': 'Stock.celery.sync_data_to_stock',
        'schedule': crontab(minute=0, hour=15, day_of_month={1, 2, 3, 4, 5}),
        'args': ()
    }
}
