import urllib3


class Http(object):
    def __init__(self):
        self.url = ''
        self.http = urllib3.PoolManager()

    def post(self, data=None):
        self.http.request(
            'POST',
            self.url,
            fields=data,
            headers=None
        )
        return 0

    def get(self, data=None):
        self.http.request(
            'GET',
            self.url,
            fields=data,
            headers=None
        )
        return 0
