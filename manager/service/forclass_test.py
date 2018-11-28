from manager.service.model.client import Client
import time
from mako.template import Template


class Erzi(Client):

    def image_info(self):
        print('2-----------------------------')
        images_info = self.images.list()  # 调用父类属性，获得部分数据
        images_all_info = self.images.list(all=True)  # 调用源码api获取全部数据
        im = self.images.get('dbfc48660aeb')
        print(im.attrs)
        res = {
            "info": images_info,
            "all_info": images_all_info,
        }
        return res

    def container(self):
        a = self.containers.get('zhang2')
        print(a.attrs['Config'])

    def ttt(self):
        a = self.containers
        param = {
            'hostname': 'lucas',
            'name': 'docker01'
        }
        con = self.containers.get('58b45d92ea9b  ')
        # try:
        #     top_info = con.top()
        # except Exception:
        #     return 'not runing'
        # return top_info
        print(con.logs())

    def plugin(self):
        p = self.plugins
        print(p.list(all=True))
        return 0

    def net(self):
        n = self.networks.list()
        a = self.networks.get('c0f3ca7b69')
        print(a.attrs)
        return 0


a = Erzi().net()
# print(a)
