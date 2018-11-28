from manager.service.model.networks import Networks


class ApiNetworks(object):
    def __init__(self):
        self.Networks = Networks()

    def get_networks_info(self):
        networks_info = self.Networks.networks_info()
        return networks_info

    def create_networks(self):
        return self.Networks.create()

    def del_networks(self):
        pass
