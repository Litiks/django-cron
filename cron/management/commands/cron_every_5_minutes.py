from django.core.management.base import BaseCommand, CommandError
from cron.signals import cron_every_5_minutes

class Command(BaseCommand):
    help = 'Triggers signals for business logic.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Sending signal for cron_every_5_minutes...")

        # It's butt-ugly that this code is here and not within access_log.. but I'm on a deadline!
        try:
            from access_log.context_managers import access_log_context_manager
        except:
            pass
        else:
            # set up defaults for logged models
            from django.contrib.auth import get_user_model
            access_log_context_manager.user = get_user_model().objects.get(email='aaron@litiks.com')
            access_log_context_manager.session_key = "local cron script: cron_every_5_minutes"
            access_log_context_manager.ip_address = "127.0.0.1"

        cron_every_5_minutes.send()
        print("Done.")
