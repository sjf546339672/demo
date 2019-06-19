# coding: utf-8

from tornado import gen
import requests
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


# future = gen.Future()

@gen.coroutine
def async_request(client, url):
    response = yield client.fetch(url)
    print('Fetch {} done, return code: {}'.format(url, response.code))

#
# @gen.coroutine
# def async_set_future_result():
#     global future
#     yield gen.sleep(5)
#     future.set_result(11111)



@gen.coroutine
def async_no_return():
    test = yield return_future()
    print('--------------')
    print(test)


def return_future(ioloop):
    future = gen.Future()
    ioloop.call_later(5, future.set_exception, 111)
    return future


@gen.coroutine
def return_future():
    yield gen.sleep(5)
    raise gen.Return(1111)


def sync_request(url):
    response = requests.get(url)
    print('Fetch {} done, return code: {}'.format(url, response.status_code))


def main1():
    client = AsyncHTTPClient()
    ioloop = IOLoop.current()
    for url in ['http://baidu.com', 'http://oschina.net', 'http://cnblogs.com']:
        ioloop.spawn_callback(async_request, client, url)
    ioloop.spawn_callback(async_no_return)
    # ioloop.spawn_callback(async_set_future_result)
    try:
        ioloop.start()
    except KeyboardInterrupt:
        pass


def main2():
    for url in ['http://baidu.com', 'http://oschina.net', 'http://cnblogs.com']:
        sync_request(url)

if __name__ == '__main__':
    main1()
    #main2()
