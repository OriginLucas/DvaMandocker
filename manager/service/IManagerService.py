import docker
# from manager import models


class Nidie(object):
    def __init__(self):
        print('1-------------------------------')
        self.url = "tcp://47.94.205.87:7478"
        # self.from_env = docker.from_env
        self.client = docker.DockerClient(base_url=self.url)
        self.images = self.client.images
        self.configs = self.client.configs  # 存在版本限制 1.3以上
        self.containers = self.client.containers
        self.networks = self.client.networks
        self.nodes = self.client.nodes
        self.plugins = self.client.plugins
        self.secrets = self.client.secrets
        self.swarm = self.client.swarm
        self.volumes = self.client.volumes


class Erzi(Nidie):
    def ziji(self):
        l = self.images.list()
        pass



# -----------------------------------
# todo


def docker_images(url):
    base_url = url
    client = docker.DockerClient(base_url="tcp://47.94.205.87:7478")
    images = client.api.images()  # 直接调用接口，获取image所有信息，否则只得到name
    container = client.api.containers(all=1)
    # client.containers.list()
    i = client.images.list()
    print(i)
    obj = client.containers.run()
    return obj


def docker_container(url):
    base_url = url
    client = docker.DockerClient(base_url="tcp://47.94.205.87:7478")
    container = 0
    return container

#
# b = docker_images("url")
# print(b)
# for i in b:
#     print(i["Created"])





