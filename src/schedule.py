from crontab import CronTab
import requests

my_cron = CronTab(user='jware')

job = my_cron.new(command='~/workspace/py_drink_bot/src/drink.py')
job.minute.every(1)

my_cron.write()
