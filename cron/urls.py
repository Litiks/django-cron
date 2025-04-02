from django.urls import path

from cron.views import process_frequently, process_hourly, process_daily


urlpatterns = [
    path('frequently/', process_frequently, name='frequently'),
    path('hourly/', process_hourly, name='hourly'),
    path('daily/', process_daily, name='daily'),
]
