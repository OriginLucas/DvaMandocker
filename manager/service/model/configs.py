from .client import Client

'''
    实现confg接口的功能(该功能对docker版本有特殊要求,1.3可以使用)
'''


class Configs(Client):
    def config_info(self):
        self.configs.list()
