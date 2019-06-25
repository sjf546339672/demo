# -*- coding:UTF-8 -*-

import os
from tornado import httpclient, gen, ioloop
from bs4 import BeautifulSoup
import requests


path = 'C:/Users/jife/Desktop/Documen/Tornado_demo/rrrr/'
# path = 'C:/Users/Administrator/Desktop/Documen/Tornado_demo/rrrr/'
client = httpclient.AsyncHTTPClient()
loop = ioloop.IOLoop.current()


@gen.coroutine
def http_fetch(url):
    filename = url.split('/')[-3] + '.jpg'
    with open(os.path.join(path, filename), 'wb') as f:
        response = yield client.fetch(url, streaming_callback=f.write)
        if response.code != 200:
            raise httpclient.HTTPError('Request picture error: {}'.format(response.reason))
        else:
            print('Download {} success'.format(filename))


@gen.coroutine
def work():
    # print(link_list[2]['src'])
    # loop.spawn_callback(http_fetch, link_list[2]['src'])
    url = 'https://www.quanjing.com/creative/topic/1'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    link_list = soup.select('.gallery .flex-images a img ')
    for link in link_list:
        src = link['src']
        loop.spawn_callback(http_fetch, src)


if __name__ == '__main__':
    loop.add_callback(work)
    loop.start()
    # loop.run_sync(work)




