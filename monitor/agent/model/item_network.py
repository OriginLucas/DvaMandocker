import psutil


class NetworkMonitor(object):
    def __init__(self):
        pass

    def __repr__(self):
        return "<network:msg>"

    def net_io_counters(self):
        return psutil.net_io_counters()

    def net_connection(self):
        return psutil.net_connections()

    def net_if_addrs(self):
        return psutil.net_if_addrs()

    def net_if_stats(self):
        return psutil.net_if_stats()


a = NetworkMonitor().net_connection()
print(a)
