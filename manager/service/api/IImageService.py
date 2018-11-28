from manager.service.model.images import Images

'''
    接收images处理请求的接口
    get_image_info: 获取images的相关信息
    pull_image: pull一个image
    push_image: push一个image
    del_image: 删除image
    search_image: 从docker Hub中查找相关的image
    prune_image: 删除未使用的image
'''


class ApiImages(object):
    def __init__(self, image_id=None):
        self.Images = Images()
        self.image_id = image_id

    def get_image_info(self):
        image_info = self.Images.image_info()
        return image_info
        # return self.Images.image_info()

    def get_detailed_data(self):
        # 模块接口无法使用
        pass

    def pull_image(self):
        return self.Images.pull_images(self.image_id)

    def push_image(self):
        return self.Images.push_images()

    def del_image(self):
        return self.Images.remove_images(self.image_id)

    def build_image(self):
        return self.Images.create_images()

    def search_image(self):
        return self.Images.find_images(self.image_id)

    def prune_image(self):
        return self.Images.prune_images()

    def put_image_info(self):
        self.Images.put_images_info()
        return 0



