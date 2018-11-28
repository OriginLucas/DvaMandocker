import time
import datetime
import socket
h = socket.gethostname()
ip = socket.gethostbyname(h)
print(h, ip)


class CacheFile(object):
    def __init__(self):
        pass

    def _filename(self):
        ip = socket.gethostbyname(h)
        host = socket.gethostname()
        redate = datetime.datetime.now()
        date = str(redate.year) + '-' + str(redate.month) + '-' + str(redate.day)
        filename = date + ':' + str(ip) + ':' + str(host)
        return filename

    def store(self, msg):
        filename = self._filename()
        with open(filename, 'ab') as fd:
            fd.write(msg)
        return fd


class TimingSend(object):  # 交给调度器实现
    def __init__(self):
        pass

    def send(self, filename):
        with open(filename, 'r') as fd:
            pass