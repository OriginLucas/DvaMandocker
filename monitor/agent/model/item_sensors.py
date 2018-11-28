import psutil

# 传感器信息，包括物理设备的温度等指标


class SensorsMonitor(object):
    def __init__(self):
        pass

    def __repr__(self):
        return "<sensors:msg>"

    def temperatures(self):
        return psutil.sensors_temperatures()

    def fans(self):
        return psutil.sensors_fans()

    def battery(self):
        return psutil.sensors_battery()