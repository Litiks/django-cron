from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cron.signals import cron_frequently, cron_every_5_minutes, cron_hourly, cron_daily

""" Note: these views should only be used with something like elastic beanstalk. If you enable them, be sure to make their inclusion conditional to the environment being an EB worker environment. """

def setup_access_logs():
    # It's butt-ugly that this code is here and not within access_log.. but I'm on a deadline!
    try:
        from access_log.context_managers import access_log_context_manager
    except:
        pass
    else:
        # set up defaults for logged models
        from django.contrib.auth import get_user_model
        access_log_context_manager.user = get_user_model().objects.get(email='aaron@litiks.com')
        access_log_context_manager.session_key = "local cron script: cron_frequently"
        access_log_context_manager.ip_address = "127.0.0.1"

@csrf_exempt
def process_frequently(request):
    setup_access_logs()
    cron_frequently.send()
    return HttpResponse("ok")

@csrf_exempt
def process_every_5_minutes(request):
    setup_access_logs()
    cron_every_5_minutes.send()
    return HttpResponse("ok")

@csrf_exempt
def process_hourly(request):
    setup_access_logs()
    cron_hourly.send()
    return HttpResponse("ok")

@csrf_exempt
def process_daily(request):
    setup_access_logs()
    cron_daily.send()
    return HttpResponse("ok")
