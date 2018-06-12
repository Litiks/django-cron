from django.conf.urls import url
from cron.views import process_frequently, process_hourly, process_daily

urlpatterns = [
    url(r'^frequently/$', process_frequently, name='frequently'),
    url(r'^hourly/$', process_hourly, name='hourly'),
    url(r'^daily/$', process_daily, name='daily'),
]
