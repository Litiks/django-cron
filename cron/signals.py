"""
    We use a trigger mechanism for cron jobs. 
    Basically there are lots of times that we might want some code to run hourly, but it seems a bit messy to have a bunch of business logic in the server's cron script. 
    The solution then, is to have a single cron script, which triggers a signal that any other business logic can listen to. Presto; one and done.
"""
import uuid

class Signal(object):
    """ This signal works a little differently than the logic at django.dispatch.signals. 
        Namely: why do we need a 'sender' class. There's a lot of bloat in the django class that we just don't need here.
    """
    def __init__(self):
        self.receivers = {}

    def connect(self, fn, dispatch_uid=None):
        # we use dispatch_uids to help ensure that we don't call the same receiver twice unintentionally.
        if not dispatch_uid:
            dispatch_uid = uuid.uuid4().hex

        self.receivers[dispatch_uid] = fn

    def send(self, **kwargs):
        # call the receivers
        results = []
        for fn in self.receivers.values():
            result = fn(**kwargs)
            results.append(result)

        return results

cron_frequently = Signal()
cron_every_5_minutes = Signal()
cron_hourly = Signal()
cron_daily = Signal()
