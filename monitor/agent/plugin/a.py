import datetime
import psutil
import time
import sched


class tes(object):
    def __init__(self):
        pass

    def a(self):
        print('trigger')
        return 0


def s():
    tes().a()
    resch = sched.scheduler(time.time, time.sleep)
    resch.enter(2, 0, s,)
    resch.run()
    return 0


def pid():
    p = psutil.pids()
    for i in p:
        print(psutil.Process(i).name(), psutil.Process(i).status())


pid()
