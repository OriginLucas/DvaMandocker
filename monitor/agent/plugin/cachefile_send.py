# 实现缓存文件中的监控数据的发送 ，时间间隔较大
from ..model.http import Http


class SendCacheFile(Http):
    def __init__(self):
        super(SendCacheFile, self).__init__()

    def send(self, fd):
        res = self.post(fd)
        return res
