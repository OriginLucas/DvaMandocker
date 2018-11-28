import docker


class Client(object):

    def __init__(self):
        # todo
        # 变量暂时这样写
        self.url = "tcp://47.94.205.87:7478"
        self.from_env = docker.from_env
        self.client = docker.DockerClient(base_url=self.url)
        self.images = self.client.images
        self.configs = self.client.configs  # 存在版本限制 1.3以上
        self.containers = self.client.containers
        self.networks = self.client.networks
        self.nodes = self.client.nodes
        self.plugins = self.client.plugins  # 存在版本限制
        self.secrets = self.client.secrets
        self.swarm = self.client.swarm
        self.volumes = self.client.volumes

    def _connect_to_docker(self):
        base_url = self.url
        return 0

    def _close(self):
        return self.client.close()

    def _df(self):
        return self.client.df()

    def _events(self):
        return self.client.events()

    def _info(self):
        return self.client.info()

    def _ping(self):
        return self.client.ping()

    def _version(self):
        return self.client.version()
