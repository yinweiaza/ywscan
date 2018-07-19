# coding=utf-8
"""
    url 管理器；
"""


class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def add_new_url(self, url):
        """
        添加新网址；
        :param url:
        :return:
        """
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def get_new_url(self):
        """
        获取新的网址；
        :return:
        """
        url = self.newUrls.pop()
        if not url:
            self.oldUrls.add(url)
        return url

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.newUrls) != 0

