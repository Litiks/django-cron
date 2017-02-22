# django-cron
Adds signals for simple cron-based automation

Basically there are lots of times that we might want some code to run hourly, but it seems a bit messy to have a bunch of business logic in our server's cron script. 

The solution then, is to have a single cron command, which triggers a signal within the project that any other business logic can listen to. Presto; one and done.


Install
-------

- using pip: `pip install https://github.com/Litiks/django-cron/archive/master.zip`
- or: add to your requirements.txt: `-e git+https://github.com/Litiks/django-cron.git#egg=django-cron`
- or: copy the 'cron' folder to your python working directory


Integrate
---------

1. Add 'cron' to your settings.INSTALLED_APPS
2. Add to your crontab:

```
* * * * *      . /path_to_project/_env/bin/activate; python /path_to_project/code/manage.py cron_frequently > /dev/null
0 * * * *      . /path_to_project/_env/bin/activate; python /path_to_project/code/manage.py cron_hourly > /dev/null
0 * * * *      . /path_to_project/_env/bin/activate; python /path_to_project/code/manage.py cron_daily > /dev/null
```


Usage
-----

Add signal listeners within your models.py, defining functions that should be run.

```
from cron.signals import cron_daily
def myfn():
    # do something
cron_daily.connect(myfn)
``` 

