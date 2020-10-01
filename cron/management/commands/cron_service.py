import time

from django.core.management.base import BaseCommand, CommandError
from cron.signals import cron_frequently, cron_hourly, cron_daily

class Command(BaseCommand):
    help = 'Service which triggers signals for business logic.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Starting the cron service...")

        # It's butt-ugly that this code is here and not within access_log.. but I'm on a deadline!
        try:
            from access_log.context_managers import access_log_context_manager
        except:
            pass
        else:
            # set up defaults for logged models
            from django.contrib.auth import get_user_model
            access_log_context_manager.user = get_user_model().objects.get(email='aaron@litiks.com')
            access_log_context_manager.session_key = "local cron script: cron_daily"
            access_log_context_manager.ip_address = "127.0.0.1"

        while True:
            t = time.time()
            print('triggering cron_frequently...')
            cron_frequently.send()
            print('triggering cron_frequently. done.')

            # minute of the hour
            minute = (t//60) % 60
            # hour of the day
            hour = (t//3600) % 24

            if minute == 0:
                # it's the first minute of the hour
                print('triggering cron_hourly...')
                cron_hourly.send()
                print('triggering cron_hourly. done.')

            if minute == 5 and hour == 5:
                # 5:05am (utc?)
                print('triggering cron_daily...')
                cron_daily.send()
                print('triggering cron_daily. done.')

            time.sleep(30)

        print("Cron service is stopping. You should usually not see this.")
