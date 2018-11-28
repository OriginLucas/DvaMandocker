from manager import models
from manager.service.model.client import Client


class Images(Client):
    def __init__(self):
        super(Images, self).__init__()

    def image_info(self):
        # 获取images信息，调用list（）返回image
        images_info = self.images.list()  # 调用父类属性，获得部分数据
        # images_all_info = self.client.api.images(all=True)  # 调用源码api获取全部数据
        images_all_info = self.images.list(all=True)
        res = {
            "info": images_info,
            "all_info": images_all_info,
        }
        return res

    def put_images_info(self):
        # 将images信息存入数据库中
        images_all_info = self.image_info()["all_info"]
        for unit in images_all_info:
            if models.DockerImages.objects.filter(image_id=unit.attrs["Id"]):  # 判断表中是否有记录
                continue
            models.DockerImages.objects.create(
                containers=unit.attrs["Containers"], image_created=unit.attrs["Created"],
                image_id=unit.attrs["Id"], image_lab=unit.attrs["Labels"], parent_id=unit.attrs["ParentId"],
                repo_digests=unit.attrs["RepoDigests"], repo_tags=unit.attrs["RepoTags"],
                shared_size=unit.attrs["SharedSize"], size=unit.attrs["Size"],
                virtual_size=unit.attrs["VirtualSize"])
        return 0

    def get_images_info(self, image_id=None, image_name=None):
        # 从数据库中获取images信息
        params = {
            'image_id': image_id,
            'image_name': image_name,
        }
        sig = params['image_id'] if params['image_id'] else params['image_name']
        smart_info = self.image_info()["info"]
        all_info = self.image_info()["all_info"]
        model_info = models.DockerImages.objects.filter(sig)
        return smart_info

    def del_images_info(self, image_id):
        # 删除数据库信息
        # todo
        models.DockerImages.objects.filter(image_id=image_id).delete()
        raise 0

    def pull_images(self, image_name):
        self.images.pull(image_name)

    def push_images(self):
        self.images.push()

    def remove_images(self, image_id):
        # todo

        self.del_images_info(image_id)
        self.images.remove(image_id)
        raise 0

    def create_images(self):
        pass

    def find_images(self, term):
        self.images.search()
        raise 0

    def prune_images(self):
        self.images.prune()
        raise 0

