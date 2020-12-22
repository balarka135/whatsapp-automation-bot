from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from honey import send_l



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_l, 'interval', hours=2)

sched.start()