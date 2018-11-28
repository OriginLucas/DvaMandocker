import psutil
from .agent_item import ActiveItems


class Host(object):
    def __init__(self):
        self.items = ActiveItems.get_item()

    def cpu(self):
        a = psutil.cpu_times()
        b = psutil.cpu_percent(interval=1, percpu=True)
        c = psutil.cpu_stats()
        return 0

    def memory(self):
        a = psutil.virtual_memory()
        b = psutil.swap_memory()
        return 0

    def swarm(self):
        pass

    def disk(self):
        a = psutil.disk_usage('/')
        b = psutil.disk_partitions()
        return 0

    def network(self):
        return 0
