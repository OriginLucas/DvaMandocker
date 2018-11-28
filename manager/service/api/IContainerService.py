from manager.service.model.containers import Containers

class ApiContainers(object):
    def __init__(self):
        self.container = Containers()

    def get_container_info(self):
        return self.container.get_container_info()

    def create_containers(self, **kwargs):
        param = kwargs['']
        return self.container.containers_create(param)

    def handle_containers(self, option, container_id):
        container_id = container_id
        return self.container.container_service()

    def alter_container(self):
        pass