# agent 主进程调度器，用于调度agent主要功能
import time
import sched
from .agent_send import Send
from .agent_cachefile import CacheFile
from .agent_item import ActiveItems


class SchedulerAgent(object):
    def __init__(self):
        self.schedule = sched.scheduler(time.time, time.sleep)

    def timing_get_active(self):
        # 向server获取items列表信息
        ActiveItems().get_item()
        self.schedule.enter(600, 0, self.timing_get_active)
        self.schedule.run()

    def timing_send(self):
        # 定时收集、发送
        Send().send_msg()
        self.schedule.enter(30, 0, self.timing_send)
        self.schedule.run()
