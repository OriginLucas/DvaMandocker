# 主动建立连接，向server请求active——items监控项列表
from .http import Http


class ActiveItems(Http):
    def __init__(self):
        super(ActiveItems, self).__init__()

    def get_item(self):
        items = self.get()
        return items
