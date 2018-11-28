# 用于收集监控数据项
import psutil
from concurrent.futures import ThreadPoolExecutor
import queue
import json
import time
from monitor.agent.model.host import Host


class Collect(Host):
    def __init__(self):
        super(Collect, self).__init__()

    def collect_msg(self):
        res = CollectRes()
        res.cpu_info = self.cpu()
        res.memory_info = self.memory()
        res.disk_info = self.disk()
        res.network_info = self.network()
        return res


class CollectRes(object):
    # 定义数据对象
    def __init__(self):
        # todo
        self.host = '12.34.123.5'
        self.timestamp = time.time()
        self.cpu_info = None
        self.memory_info = None
        self.disk_info = None
        self.network_info = None

    def __repr__(self):
        return "<%s: '%s' at %s>" % (self.__class__.__name__, self.host, self.timestamp)


a = Collect()
print(a.collect_msg())
