# 用于将数据发送到指定url中
from .agent_collect import Collect
import queue
from .http import Http
from monitor.agent.model.agent_cachefile import CacheFile


class Send(Http):
    def __init__(self):
        super(Send, self).__init__()
        self.q = queue.Queue(maxsize=1024)
        self.url = ''

    def send_msg(self, msg=None):
        while msg is None:
            msg = self.__rev_msg()
        repo = self.post(msg)
        if repo:  # 发送失败执行缓存操作
            CacheFile().store(msg)
        return 0

    def __rev_msg(self):
        # 用于调用收集数据的类方法
        msg = Collect().collect_msg()
        res = msg
        return res
