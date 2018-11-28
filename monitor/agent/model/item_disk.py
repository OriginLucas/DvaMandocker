import psutil


class DiskMonitor(object):
    def __init__(self):
        self.disk_partitions = self.disk_partitions()

    def __repr__(self):
        return "<disk:msg>"

    def disk_partitions(self):
        return psutil.disk_partitions()

    def disk_usage(self, path='/'):
        return psutil.disk_usage(path=path)

    def disk_io_counters(self):
        return psutil.disk_io_counters()


a = DiskMonitor()
print(a.disk_partitions)
