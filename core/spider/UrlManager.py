# coding=utf-8
"""
    url 管理器；
"""


class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def add_new_url(self, url):
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def get_new_url(self):
        url = self.newUrls.pop()
        if not url:
            self.oldUrls.add(url)
        return url
