# 对agent端的plug 程序的调度
import sched
from .cachefile_send import SendCacheFile
from .heartbeat import Heartbeat
import time


class SchedulerPlugin(object):
    def __init__(self):
        self.schedule = sched.scheduler(time.time, time.sleep)

    def timing_send_cachefile(self):
        SendCacheFile().send()
        self.schedule.enter(86400, 0, self.timing_send_cachefile)
        self.schedule.run()

    def timing_heartbeat(self):
        Heartbeat().check()
        self.schedule.enter(120, 0, self.timing_heartbeat)
        self.schedule.run()
