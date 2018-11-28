import psutil


class CpuMonitor(object):
    def __init__(self):
        self.cpu_times = self.cpu_times()
        self.cpu_percent = self.cpu_percent()
        self.cpu_count = self.cpu_count()
        self.cpu_status = self.cpu_status()
        self.cpu_fred = self.cpu_fred()

    def __repr__(self):
        return "<cpu:msg>"

    def cpu_times(self):  # 返回元组，包含cpu在给定模式下花费的时间
        return psutil.cpu_times()

    def cpu_percent(self):
        return psutil.cpu_percent(interval=1, percpu=True)

    def cpu_count(self):
        return psutil.cpu_count()

    def cpu_status(self):
        return psutil.cpu_stats()

    def cpu_fred(self):  # 返回cpu频率
        return psutil.cpu_freq()


cpu = CpuMonitor()
print(cpu.cpu_fred())
