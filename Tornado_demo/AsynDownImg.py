# coding:UTF-8

#   'https://www.quanjing.com/creative/topic/1'

import time
from tornado import gen, httpclient, ioloop
from requests import get


# class SynSpider(object):
#     def __init__(self, urls):
#         self.urls = urls
#
#     def fetch_url(self, url):
#         r = get(url)
#         return r.content
#
#     def handle_page(self, html):
#         print(html)
#
#     def run(self):
#         for url in urls:
#             html = self.fetch_url(url)
#             self.handle_page(html)

class AsyncSpider(object):
    def __init__(self,urls):
        self.urls = urls

    @gen.coroutine
    def fetch_url(self,url):
        try:
            response = yield httpclient.AsyncHTTPClient().fetch(url)
        except:
            print('fetch fail')
            raise gen.Return('')
        raise gen.Return(response.boby)

    def handle_page(self, html):
        print(html)

    @gen.coroutine
    def _run(self):
        for url in urls:
            html = yield self.fetch_url(url)
            self.handle_page(html)
    def run(self):
        io_ioop = ioloop.IOLoop.current()
        # io_ioop.run_sync(self.run)


if __name__ == '__main__':
    urls = ['https://www.quanjing.com/creative/topic/1']
    t1 = time.time()
    s = AsyncSpider(urls)
    s.run()
    t2 = time.time()
    print(t2-t1)

# import os
# path = 'C:/Users/jife/Desktop/Documen/Tornado_demo/rrrr/'
# e_names = set(os.listdir(path))
# print(e_names)










