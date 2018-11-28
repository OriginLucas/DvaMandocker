from manager import models
from manager.service.model.client import Client


class Networks(Client):
    def __init__(self):
        super(Networks, self).__init__()

    def create(self, **kwargs):
        network = self.networks.create(name=kwargs['name'], driver=kwargs['driver'],
                                       scope=kwargs['scope'],)
        return network.short_id

    def networks_info(self, network_id=None):
        return self.networks.list()

    def get_networks_info(self):
        network_list = self.networks_info()
        model_info = models.DockerNetworks.objects.get()
        return network_list

    def put_networks_info(self, network_id=None):
        # todo
        all_info = self.networks_info(network_id=network_id)
        for unit in all_info:
            models.DockerNetworks.objects.create(id=unit)
        return all_info
