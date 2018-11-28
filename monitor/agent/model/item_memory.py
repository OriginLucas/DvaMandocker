import psutil


class MemoryMonitor(object):
    def __init__(self):
        self.virtual_memory = self.virtual_memory()
        self.swap_memory = self.swap_memory()

    def __repr__(self):
        return "<memory:msg>"

    def virtual_memory(self):
        return psutil.virtual_memory()

    def swap_memory(self):
        return psutil.swap_memory()
