#coding:utf-8





# import tornado.web
# from tornado import gen
# from tornado import httpclient
# from tornado import ioloop
#
# class AsyncHandler(tornado.web.RequestHandler):
#     @gen.coroutine
#     def get(self, *args, **kwargs):
#         print('port')
#         client = httpclient.AsyncHTTPClient()
#         data = yield client.fetch('http://www.google.com')
#         print('finish',data)
#         self.finish('6666666')
#
#
# application = tornado.web.Application([
#         (r'/',AsyncHandler),
#     ])
# if __name__ == '__main__':
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()



# def add(x,y):
#     yield x+y
#
# def main():
#     r = yield add(3,6)
#     print r
#     yield
#
# a = next(main())
# for s in a:
#     print s

# import tornado
# import tornado.web
# import tornado.ioloop
#
# class MainHandeler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         self.write("hello word!!!!!")
#         self.finish()
#
#
#
# if __name__ == '__main__':
#     application = tornado.web.Application([
#         (r'/',MainHandeler),
#     ])
#     application.listen(8888)
#     tornado.ioloop.IOLoop.current().start()















# import time
# import logging
# import tornado.ioloop
# import tornado.web
# import tornado.options
# from tornado import gen
#
# tornado.options.parse_command_line()
#
# class MainHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         self.write("hellow word")
#         self.finish()
#
#
#
# class NoBlockHandler(tornado.web.RequestHandler):
#     @gen.coroutine
#     def get(self):
#         yield gen.sleep(1)
#         self.write("NoBlocking Request")
#
# class BlockingHandler(tornado.web.RequestHandler):
#     def get(self):
#         time.sleep(1)
#         self.write("Blocking Request")
#
# # def make_app():
# #     return tornado.web.Application([
# #         (r'/',MainHandler),
# #         (r'/block',BlockingHandler),
# #         (r'/noblock',NoBlockHandler),
# #     ],autoreload=True)
#
# if __name__ == '__main__':
#     application = tornado.web.Application([
#                 (r'/',MainHandler),
#                 (r'/block',BlockingHandler),
#                 (r'/noblock',NoBlockHandler),
#     ],autoreload=True)
#     application.listen(8888)
#     tornado.ioloop.IOLoop.current().start()










# import time
# import logging
# import tornado.ioloop
# import tornado.web
# import tornado.options
# from tornado import gen
# from tornado.concurrent import run_on_executor
# from concurrent.futures import ThreadPoolExecutor
#
# tornado.options.parse_command_line()
#
# class MainHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         self.write("Hellow")
#         self.finish()
#
#
# class NoBlockingHnadler(tornado.web.RequestHandler):
#     executor = ThreadPoolExecutor(4)
#     @run_on_executor()
#     def sleep(self,second):
#         time.sleep(second)
#         return second
#
#     @gen.coroutine
#     def get(self):
#         second = yield self.sleep(5)
#         self.write("noBlocking Request:{}".format(second))
#
# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", MainHandler),
# #         (r"/noblock", NoBlockingHnadler),
# #     ], autoreload=True)
# if __name__ == "__main__":
#     application = tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/noblock", NoBlockingHnadler),
#     ],autoreload=True)
#     application.listen(8888)
#     # app = make_app()
#     # app.listen(8000)
#     tornado.ioloop.IOLoop.current().start()









# import os
# import time
# from celery import Celery
# from tornado import gen
#
# celery = Celery("tasks",broker="amqp://")
# celery.conf.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND','amqp')
#
# @celery.task
# def sleep(seconds):
#     time.sleep(float(seconds))
#     return seconds
#
# if __name__ == '__main__':
#     celery.start()








# import tornado.ioloop
# from tornado.gen import coroutine
# from tornado.concurrent import Future
# from tornado.httpclient import AsyncHTTPClient
# @coroutine
# def get_web():
#      http_client = AsyncHTTPClient()
#      # http_client = HTTPClient()
#      response = yield http_client.fetch("http://example.com")
#      print 'status_code is %s' % response.code
#
# @coroutine
# def asyn_sum(a, b):
#     print("begin calculate:sum %d+%d"%(a,b))
#     future = Future()
#
#     def callback(a, b):
#         print("calculating the sum of %d+%d:"%(a,b))
#         future.set_result(a+b)
#     tornado.ioloop.IOLoop.instance().add_callback(callback, a, b)
#
#     result = yield future
#
#     print("after yielded")
#     print("the %d+%d=%d"%(a, b, result))
#
# def main():
#     asyn_sum(2,3)
#     print 'haha'
#     tornado.ioloop.IOLoop.instance().start()
#
# if __name__ == "__main__":
#     main()




# LIST_INFO = []
# for i in range(200):
#     temp = {'username':"zhang"+str(i),'email':str(i)+"@163.com"}
#     LIST_INFO.append(temp)
#
# for i in LIST_INFO:
#     print(i)





# from tornado.web import Application,RequestHandler
# from tornado.ioloop import IOLoop
#
# class IndexHandler(RequestHandler):
#     def get(self):
#         self.write("hello")
#         self.set_cookie('logging','adminlaowang')
#         print(self.get_cookie('logging'))
#         print(self.cookies)
#
#
# if __name__ == '__main__':
#     app = Application([
#         (r'/',IndexHandler),
#     ])
#     app.listen(8000)
#     IOLoop.current().start()





# class Future(object):
#     def set_result(self,result):
#         self._result = result
#         self._set_done()
#
#
#     def _set_done(self):
#         self._done = True
#         if self._callbacks:
#             from tornado.ioloop import IOLoop
#             loop = IOLoop.current()
#             for cb in self._callbacks:
#                 loop.add_callback(cb,self)
#             self._callbacks = None


# import time
# print(time.ctime())


####
# import socket
#
# server_udp = socket.socket(type=socket.SOCK_DGRAM)
# ip_port = ('127.16.5.236',10086)
# server_udp.bind(ip_port)
# data,addr = server_udp.recvfrom(1024)
# server_udp.close()


# zoo = ('wolf', 'elephant', 'penguin')
# print(len(zoo))
# new_zoo = ('monkey', 'dolphin', zoo)
# print(len(new_zoo))
# print(new_zoo)
# print(new_zoo[2])
# print( new_zoo[2][2])
# print(new_zoo[2][0])





# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist = shoplist
# print(mylist)
# del shoplist[0]
#
# print  shoplist
# print  mylist
#
#
# mylist = shoplist[:]
# del mylist[0]
# print  shoplist






# import os
# import time
#
# source = ['/home/swaroop/byte', '/home/swaroop/bin']
# target_dir = '/mnt/e/backup/'
#
#
# target = target_dir + time.strftime('%Y%m%d%H%M%S')
#
#
#
# list_str = ['zz','bb','cc']
# list_str.remove('bb')
# list_str.pop()
# list_str.sort()
# list_str.reverse()
# print(list_str)




# import cPickle as p
#
# shoplistfile = 'shoplist.data'
#
# shoplist = ['apple', 'mango', 'carrot']
#
# f = file(shoplistfile,'w')
# p.dump(shoplist,f)
# f.close()
#
# del shoplist
#
# t = file(shoplistfile)
# sortedfile = p.load(t)
# print(sortedfile)



# shoplist = ['apple', 'mango', 'carrot']



# import time
#
#
# try:
#     f = file('poem.txt')
# except IOError as e:
#     print('tttt')



# listone = [2,3,4]
# listtwo = [2*i for i in listone if i>3]
# print(listtwo)


# str1 = 'rwerewrew'
#
# try:
#     int(str1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print('try内没有异常')
# finally:
#     print('执行完成')


# def not_zero(num):
#     try:
#         if num == 0:
#             raise ValueError('参数错误')
#         return num
#     except Exception as e:
#         print(e)
#
# not_zero(0)


# try:
#     for i in range(10):
#         int(i)
# except IndexError as e:
#     print(e)
# else:
#     print('***********')



# list = [1,2,3,4]
# try:
#     list.pop1()
# except AttributeError as e:
#     print('{},{}'.format(AttributeError,'您使用的属性发生错误'))
#
# print(list)




# def devide(x,y):
#     if y == 0:
#         try:
#             x / y
#         except ZeroDivisionError as e:
#             print('分母不能为0')
#     else:
#         return x / y
#
# print devide(8,0)



# import tornado.gen
# from tornado.httpclient import AsyncHTTPClient
# import json
# @tornado.gen.coroutine
# def get(self,url):
#     client = AsyncHTTPClient()
#     response = yield client.fetch(url)
#     json_data = response.body
#     data = json.load(json_data)
#     self.write(data.get("city",""))





# import sys
# text = sys.stdin.read()
# words = text.split()
# for i in words:
#     print(i)



#字典的键的删除 和 两个字典的合并
# dic = {'name':'zhangsan','age':23}
# print(dic)
# del dic["name"]
# print(dic)
#
# dic2 = {'name':'lisi'}
# dic.update(dic2)
# print(dic)



#   列表用集合进行去重然后再将其转化成列表
# list_set = [1,3,4,5,6,6,7,7,9,9]
# print(list_set)
# a = set(list_set)
# print(a)
# list2 = []
# for x in a:
#     list2.append(x)
# print(list2)


# import re
# line = 'asdf fjdk; afed, fjek,asdf, foo'
# line_list = re.split(r'[;,\s]\s*', line)
# print(line_list)



# import time
# print time.strftime('%Y%m%d%H%M%S')


# text1 = '11/27/2012'
# text2 = 'Nov 27, 2012'
#
# import re
# if re.match(r'\d+/\d+/\d+',text1):
#     print('yes')
# else:
#     print('no')
#
#
# if re.match(r'\s*',text2):
#     print('yes')
# else:
#     print('no')


# import re
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# datepat = re.compile(r'\d+/\d+/\d+')
# print(datepat.findall(text))


# import re
# text = 'UPPER PYTHON, lower python, Mixed Python'
# print( re.findall('python',text,flags=re.IGNORECASE))

# print(re.sub('python','snake',text,flags=re.IGNORECASE))
#
# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word
#     return replace
#
# print(re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE))


# parts = ['Is', 'Chicago', 'Not', 'Chicago?']
# print(' '.join(parts))
# print(','.join(parts))
# print(''.join(parts))


# def sample():
#     yield 'Is'
#     yield 'Chicago'
#     yield 'Not'
#     yield 'Chicago?'
#
# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#         size += len(part)
#     if size > maxsize:
#         yield ''.join(parts)
#     parts = []
#     size = 0
#     yield ''.join(parts)
#
# with open('filename', 'w') as f:
#     for part in combine(sample(), 32768):
#         f.write(part)





# s = '{} has {} messages.'
# print(s.format('zhangsna','32'))




# from decimal import localcontext
# from decimal import Decimal
# a = Decimal('1.3')
# b = Decimal('1.7')
# print(a / b)
#
# with localcontext() as ctx:
#  ctx.prec = 3
# print(a / b)
#
# with localcontext() as ctx:
#     ctx.prec = 15000
#     print(a / b)


# import math
# a = float('inf')
# print(a)
# print(math.isinf(a))


# from datetime import timedelta
# from datetime import datetime, timedelta
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
# 'Friday', 'Saturday', 'Sunday']
# def get_previous_byday(dayname, start_date=None):
#     if start_date is None:
#         start_date = datetime.today()
#     day_num = start_date.weekday()
#     day_num_target = weekdays.index(dayname)
#     days_ago = (7 + day_num - day_num_target) % 7
#     if days_ago == 0:
#         days_ago = 7
#     target_date = start_date - timedelta(days=days_ago)
#     return target_date



# def apply_async(func, args, callback):
#     result = func(*args)
#     callback(result)
#
#
# def print_resule(result):
#     print(result)
#
# def add(x, y):
#     return x+y
#
#
# print(apply_async(add, (2, 3), callback=print_resule))



# import fileinput
# with fileinput.input('C:\Users\jife\Desktop\Documen\Tornado_demo') as f:
#     for line in f:
#         print(f.filename(), f.lineno(), line)




# import webbrowser
# webbrowser.open('http://www.baidu.com')
# webbrowser.open('http://www.python.org')



# from http.client import HTTPConnection
# # import urlparse
#
# c = HTTPConnection('www.python.org', 80)
# c.request('HEAD', '/index.html')
# resp = c.getresponse()
#
# print('Staus',resp.status)
# for name, value in resp.getheaders():
#     print(name, value)



# import hmac
# import os
#
# def client_authenticate(connection, secret_key):
#     message = connection.recv(32)
#     hash = hmac.new(secret_key, message)
#     digest = hash.digest()
#     connection.send(digest)
#
# def server_authenticate(connection, secret_key):
#     message = os.urandom(32)
#     connection.send(message)
#     hash = hmac.new(secret_key, message)
#     digest = hash.digest()
#     response = connection.recv(len(digest))
#     return hmac.compare_digest(digest, response)





# def urlprint(protocol, host, domain):
#     url = '{}://{}.{}'.format(protocol, host, domain)
#     print(url)
# print(urlprint('http', 'www', 'baidu.com'))



# from urllib2 import urlopen
# import csv
#
# def dowprices():
#     u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
#     lines = (line.decode('utf-8') for line in u)
#     rows = (row for row in  csv.reader(lines) if len(row) == 2)
#     prices = { name:float(price) for name, price in rows}
#     return prices
#
# dowprices()


# import sys
# import unittest
# def main(out=sys.stderr, verbosity=2):
#     loader = unittest.TestLoader()
#     suite = loader.loadTestsFromModule(sys.modules[__name__])
#     unittest.TextTestRunner(out,verbosity=verbosity).run(suite)
#
# if __name__ == '__main__':
#     with open('testing.out', 'w') as f:
#         main(f)



# import fileinput
#
# with fileinput.input() as f:
#     for line in f:
#         print(line)


# import sys
#
# sys.stderr.write('It failed!\n')
# raise SystemExit(1)


# def avg(first, *args):
#     return (first + sum(args)) / (1 + len(args))
#
# print avg(1,2,3,4,5)





'''
如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来，可以像下面这样写：
'''
# _value = object()
# def spam(a, b=_value):
#     if b is _value:
#         print('No b Value supplied')
#         print(a)
#     else:
#         print('ok')
#         print(a,b)
#
# spam(1, None)




# from urllib2 import urlopen
#
# class UrlTemplate:
#     def __init__(self, template):
#         self.template = template
#
#     def open(self, **kwargs):
#         return urlopen(self.template.format_map(kwargs))
#
# yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))



# from urllib2 import urlopen
# def urltemplate(template):
#     def opener(**kwargs):
#         return urlopen(template.format_map(kwargs))
#     return opener
# yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))



# def a(i):
#
#     print("回调函数1")
#     return i**2
#
#
# def b(i):
#
#     print("回调函数2")
#     return i*2
#
#
# def res(i,f):
#     print(i,f(i))
#
#
# def main():
#     i = int(input("输入一个数字："))
#     if i > 5:
#         res(i,a)
#     else:
#         res(i,b)
#
# if __name__ == '__main__':
#     main()





# 内联回调函数
# def apply_async(func, args, callback):
#     result = func(*args)
#     callback(result)
#
#
#
# from queue import Queue
# from functools import wraps
#
# class Async:
#     def __init__(self, func, args):
#         self.func = func
#         self.args = args
#
#
# def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#         f = func(*args)
#         result_queue = Queue()
#         result_queue.put(None)
#         while True:
#             result = result_queue.get()
#             try:
#                 a = f.send(result)
#                 apply_async(a.func, a.args, callback=result_queue.put)
#             except StopIteration:
#                 break
#
#     return wrapper
#
#
#
# def add(x, y):
#     return x + y
#
# @inlined_async
# def test():
#     r = yield Async(add, (2, 3))
#     print(r)
#     r = yield Async(add, ('hello', 'world'))
#     print(r)
#     for n in range(4):
#         r = yield Async(add, (n, n))
#         print(r)
#
#     print('Goodbye')
#
#
# test()




# def ExFunc(n):
#     sum = n
#     def InFunc():
#         return sum + 1
#     return InFunc()
#
#
#
# t = ExFunc(10)
# print(t)
#
# a = ExFunc(20)
# print(a)



#   闭包
# def addx(x):
#     def addy(y):
#         return x + y
#     return addy
#
# a = addx(15)
# b = a(100)
# print(b)


# 装饰器
# def deco(func):
#     def _deco(a, b):
#         print("before myfunc() called.")
#         ret = func(a, b)
#         print("after myfunc() called. result:{}".format(ret))
#         return ret
#     return _deco
#
#
# @deco
# def myfunc(c, d):
#     print('myfunc() called')
#     return c + d
#
# myfunc(2,4)
# myfunc(1,3)

#  对带参数的函数进行装饰
# def demo(func):
#     def demo1(a, b):
#         ret = func(a, b)
#         print('这个值是：{}'.format(ret))
#         return ret
#     return demo1
#
#
# @demo
# def wrap(a, b):
#     return a * b
#
#
# wrap(5,6)



# 第四步 ：让装饰器带参数

# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print('before {} called [{}]'.format(func.__name__, arg))
#             func()
#             print('after {} called [{}]'.format(func.__name__, arg))
#         return __deco
#     return _deco
#
#
# @deco("mymodule")
# def myfunc():
#     print("myfunc() called")
#
#
# @deco("mymodule2")
# def myfunc2():
#     print("myfunc2() called")


# myfunc()
# myfunc2()











#多线程 多进程
# import time
# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#         time.sleep(1)
#
# from  threading import Thread
# t = Thread(target=countdown, args=(10,))
# t.start()

# if t.is_alive:
#     print('alive')
# else:
#     print('GameOver')



# from threading import Thread
# import time
# class CountdownTask:
#     def __init__(self):
#         self._running = True
#
#     def terminate(self):
#         self._running = False
#
#     def run(self, n):
#         while self._running and n > 0:
#             print(n)
#             n -= 1
#             time.sleep(2)
#
# c = CountdownTask()
# t = Thread(target=c.run, args=(10,))
# t.start()
# c.terminate()   # Signal termination
# t.join()        #  Wait for actual termination (if needed)




# from threading import Thread
# import time
#
# class IOTask:
#     def terminate(self):
#         self._running = False
#
#     def run(self, sock):
#         sock.settimeout(5)
#         while self._running:
#             try:
#                 data = sock.recv(8192)
#                 break
#             except sock.timeout:
#                 continue
#         return



# from threading import Thread
# import time
# class CountdownThead(Thread):
#     def __init__(self, n):
#         super().__init__()
#         self.n = 0
#
#     def run(self):
#         while self.n > 0:
#             print(self.n)
#             time.sleep(5)
#
# c = CountdownThead(5)
# c.start()



# 已经启动一个线程 ，确定它是不是真的已经开始运行

# from threading import Thread, Event
# import time
#
# def countdown(n, started_evt):
#     print('countdown starting')
#     started_evt.set()
#     while n > 0:
#         print(n)
#         n -= 1
#         time.sleep(10)
#
# # Create the event object that will be used to signal startup
# started_evt = Event()
#
# # Launch the thread and pass the startup event
# print('Launching countdown')
# t = Thread(target=countdown, args=(10,started_evt))
# t.start()
#
# # Wait for the thread to start
# started_evt.wait()
# print('countdown is running')



# 你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据

# from queue import Queue
# from threading import Thread
#
#
# def producer(out_q):
#     data = {
#         'name':'zhangsna',
#         'age':123
#     }
#     while True:
#         out_q.put(data)
#
# def consumer(in_q):
#     while True:
#         data = in_q.get()
#
#
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=producer, args=(q,))
# t1.start()
# t2.start()



# class Card(object):
#
#     def __init__(self, cards):
#         self._cards = cards
#
#     def __iter__(self):
#         return iter(self._cards)
#
#     # def next(self):
#     #     for card in self._cards:
#     #         yield card
#
#
# if __name__ == '__main__':
#     card = Card([1,2,3,4])
#     for i in card:
#         print i



# info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for index,i in enumerate(info):
#     print(i+1)
#     b.append(i+1)
# print(b)
# for index,i in enumerate(info):
#     info[index] +=1
# print(info)



# import sqlite3
#
# conn = sqlite3.connect('test.db')
# print('tttttt')


#  正则表达式
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*)', line, re.M|re.I)
# print(matchObj.group())
# print('========================')
# print(matchObj.group(1))
# print('----------------------')
# print(matchObj.group(2))




# user = {'zhangsan': {'name': 'zhangsan', 'age': 18, 'job': 'student'}}
#
# user1 = {'name': 'zhangsan', 'age': 18, 'job': 'student'}
# for i in user.values():
#     print(type(i))
#     print(i['name'])




# user = {'a':1,'b':2}
# user.pop('zhangsan')
# print(user)

# user.pop('a')
# print(user)


# for v in user.keys():
#     print(v)
    # for t in v.items():
    #     print(t[0])



# file_path = r'C:\Users\jife\Desktop\agent-ng-master-1dd4d97c8b5d9478509350e778b0b46a27ebb8a4'
# import os
# print(os.path.basename(file_path))



# user1 = {
#     1111:{ 'a':1, 'b':2,  'c':3},
#     2222:{'a':1, 'b':2, 'c':3}
# }
#
# print(user1[1111]['a'])


# user = {'a':1,'b':2}
# t = user.__eq__(0)
# v = user.__hash__()





# # coding:utf-8
# import sqlite3
# import pytest
#
#
# class DbUser(object):
#
#
#     def __init__(self):
#         self.conn = sqlite3.connect(':memory:')
#         self.c = self.conn.cursor()
#         self.c.execute('''CREATE TABLE USER
#                   (NAME           TEXT    NOT NULL,
#                    AGE            INT     NOT NULL,
#                    JOB           TEXT    NOT NULL);
#
#                       ''')
#
#
#     def insert(self, data):
#         for i in data.values():
#             print(i)
#             self.c.execute("INSERT INTO USER (NAME, AGE, JOB) VALUES ('{}', {}, '{}' )".format(i['name'], i['age'], i['job']))
#             self.conn.commit()
#
#     def get(self, data):
#         getdata = self.c.execute("SELECT name, age, job  from USER WHERE name = '{}'".format(data))
#         tuple_data = getdata.fetchone()
#         if tuple_data:
#             return {'name':tuple_data[0], 'age':tuple_data[1], 'job':tuple_data[2]}
#         else:
#             return {}
#
#     def updata(self, name, data):
#         get_data_one = self.get_data(name)
#         if get_data_one:
#             query = ["{}='{}'".format(key, value) for key, value in data.items()]
#             self.c.execute("UPDATE USER  SET {} where name='{}'".format(','.join(query), name))
#         else:
#             print('数据不存在')
#
#     def delete(self, data):
#         data_one = self.get_data(data)
#         if data_one:
#             self.c.execute("DELETE FROM USER WHERE name='{}'".format(data))
#         else:
#             print("不存在")
#
#
# a = DbUser()
# a.insert({'name': 'zhangsan', 'age': 18, 'job': 'student'})
# a.get('zhangsan')
# a.updata('zhangsan',{'age': 48, 'job':'English'})
# a.delete('zhangsan11')
# result = a.get('zhangsan')
# print(result)



# import pytest
# @pytest.mark.parametrize("data", [{'name': 'zhangsan', 'age': 18, 'job': 'student'}, {'name': 'zhangsan', 'age': 18, 'job': 'student'}])
# def test_insert(data):
#     print(data)



import pytest



