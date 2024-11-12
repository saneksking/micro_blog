from urllib.parse import urlparse


class UrlParser:

    @classmethod
    def parse_url(cls, url):
        url = str(url)
        if url is not None:
            o = urlparse(url)
            user_id = o.path.lstrip('/')
            return user_id
        return url

    @classmethod
    def parse(cls, url):
        url = str(url)
        if url.endswith('/'):
            url = url.rstrip('/')
        data = urlparse(url).path.split("/")[-1]
        return data

    def __call__(self, url):
        return self.parse_url(url)
