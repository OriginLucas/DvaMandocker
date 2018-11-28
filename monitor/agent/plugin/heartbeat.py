# 用于实现对agent主进程的监控

import psutil
import subprocess


class Heartbeat(object):
    def __init__(self):
        pass

    def _get_pid(self):
        pid = ''
        return pid

    def check(self):
        pid = self._get_pid()
        process = psutil.Process(pid)
        if process.status() == 'running':
            return 1
        else:
            RestorePid().restart(pid)
            return 0


class RestorePid(object):
    def __init__(self):
        pass

    def restart(self, pid):
        pass
