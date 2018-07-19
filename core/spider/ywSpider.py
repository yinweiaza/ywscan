"""
  计划开发成超级爬虫；
"""
# coding:utf-8
from core.spider.UrlManager import  UrlManager
from urllib.parse import urlparse
from urllib.request import Request,urlopen

class Spider(object):
    def __init__(self, rooturl, maxdepth = 10):
        self.urls = UrlManager()
        self.rootUrl = rooturl              # 开始爬取地址；
        self.maxdepth = maxdepth            # 最大爬取深度
        self.depth = 0                      # 当前爬取深度

    def craw(self):
        """
        爬虫进入口；
        :return:
        """
