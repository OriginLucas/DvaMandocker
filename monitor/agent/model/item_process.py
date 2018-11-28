import psutil


class ProcessMonitor(object):
    def __init__(self):
        pass

    def __repr__(self):
        return "<process:msg>"

    def pid_list(self):
        return psutil.pids()
