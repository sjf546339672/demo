# coding:utf-8


from __future__ import unicode_literals
from attr import attrs, attrib
import pytest


# def test_answer():
#     print('--------------')
#     assert 3 in [3, 4, 5]
#
#
# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         3 / 0
#
#
# def my_func():
#     raise ValueError("Exception 123 raised")
#
#
# def test_match():
#     with pytest.raises(ValueError, match=r'.*123*.'):
#         my_func()


# 分组测试
# @pytest.mark.g1
# def test_func1():
#     pass
#
#
# @pytest.mark.g2
# def test_func2():
#     pass
#
#
# @pytest.mark.g1
# def test_func3():
#     pass
#
#
# @pytest.mark.g2
# def test_func4():
#     pass
#
#
# @pytest.mark.g1
# def test_func5():
#     pass


# def binary_search(sorted_array, val):
#     """二分法"""
#     if not sorted_array:
#         return -1
#     beg = 0
#     end = len(sorted_array) - 1
#
#     while beg <= end:
#         mid = int(beg + end) / 2
#         if sorted_array[mid] == val:
#             return mid
#         elif sorted_array[mid] > val:
#             end = mid - 1
#         else:
#             beg = mid + 1
#     return -1
#
#
# def test_binary_search():
#     """二分法的测试"""
#     a = list(range(10))
#
#     # 正常值
#     assert binary_search(a, 1) == 1
#     assert binary_search(a, -1) == -1
#
#     # 异常值
#     assert binary_search(None, 1) == -1
#
#     # 边界值
#     assert binary_search(a, 0) == 0


# class test():
#     name = "hello"
#
#
# t = test()
#
#
# def test_two():
#     assert hasattr(t, 'name')


# pytest --resultlog=path   # 创建结果日志格式文件


# 从python代码调用pytest
# class MyPlugin(object):
#     def pytest_sessionfinish(self):
#         print("test run reporting finishing")
#
#
# pytest.main(["-qq"], plugins=[MyPlugin()])


# def func():
#     return 3
#
#
# def test_func():
#     assert func() == 3


# def test_set_comparison():
#     set1 = set("1308")
#     set2 = set("1308")
#     assert set1 == set2

# @pytest.fixture
# def smtp_connection():
#     import smtplib
#     return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#
#
# def test_ehlo(smtp_connection):
#     response, msg = smtp_connection.ehlo()
#     assert response == 250
#     assert 0


# @pytest.fixture
# def make_customer_record():
#     def _make_customer_record(name):
#         return {
#             "name": name,
#             "orders": []
#         }
#
#     return _make_customer_record
#
#
# def test_customer_records(make_customer_record):
#     customer_1 = make_customer_record("Lisa")
#     customer_2 = make_customer_record("Mike")
#     customer_3 = make_customer_record("Meredith")


# @pytest.fixture(params=[0, 1], ids=["s", "h"])
# def a(request):
#     return request.param
#
#
# def test_a(a, capsys):
#     print(capsys)
#     print(type(a))
#     print(a)
#     pass


# def i(f):
#     if f == 0:
#         return "eggs"
#     else:
#         return None
#
#
# @pytest.fixture(params=[0, 1], ids=i)
# def b(request):
#     return request.param
#
#
# def test_b(b):
#     pass


# 通过fixture实例自动分组测试
# @pytest.fixture(scope="module", params=["mod1", "mod2"])
# def modarg(request):
#     param = request.param
#     print("  SETUP modarg %s" % param)
#     yield param
#     print("  TEARDOWN modarg %s" % param)
#
#
# @pytest.fixture(scope="module", params=[1, 2])
# def otherarg(request):
#     param = request.param
#     print("  SETUP otherarg %s" % param)
#     yield param
#     print("  TEARDOWN otherarg %s" % param)


# def test_0(otherarg):
#     print("  RUN test0 with otherarg %s" % otherarg)


# def test_1(modarg):
#     print("  RUN test1 with modarg %s" % modarg)


# def test_2(otherarg, modarg):
# print("  RUN test2 with otherarg %s and modarg %s" % (otherarg, modarg))


# class DB(object):
#     def __init__(self):
#         self.intrans_action = []
#
#     def begin(self, name):
#         self.intrans_action.append(name)
#
#     def rollback(self):
#         self.intrans_action.pop()
#
#
# @pytest.fixture(scope="module")
# def db():
#     return DB()
#
#
# class TestClass(object):
#     @pytest.fixture(autouse=True)
#     def transact(self, request, db):
#         db.begin(request.function.__name__)
#         yield
#         db.rollback()
#
#     def test_method1(self, db):
#         assert db.intrans_action == ["test_method1"]
#
#     def test_method2(self, db):
#         assert db.intrans_action == ["test_method2"]


# @pytest.mark.xfail()
# def test_func1():
#     assert 6 in [3, 4, 5]
#
#
# def test_func2():
#     assert 4 in [3, 4, 5]


# @pytest.mark.xfail
# def test_hello():
#     assert 0
#
#
# @pytest.mark.xfail(run=False)
# def test_hello2():
#     assert 0
#

#
# @pytest.mark.xfail("hasattr(os, 'sep')")
# def test_hello3():
#     assert 0
#
#
# @pytest.mark.xfail(reason="bug 110")
# def test_hello4():
#     assert 0
#
#
# @pytest.mark.xfail('pytest.__version__[0] != "17"')
# def test_hello5():
#     assert 0
#
#
# def test_hello6():
#     pytest.xfail("reason")
#
#
# @pytest.mark.xfail(raises=IndexError)
# def test_hello7():
#     x = []
#     x[1] = 1


# def setup_function(t):
#     print("setting up %s" % t)
#
#
# def test_func1():
#     assert True
#
#
# def test_func2():
#     assert False

# import sys
# #
# #
# def test_myoutput(capsys):
#     print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"


# import time
# import sys
# for i in range(5):
#     print('11111')
#     print i,
#     # sys.stdout.flush()
#     time.sleep(1)
# print('rrrr')





# def api_v1():
#     warnings.warn(UserWarning('api v1, should use functions from v2'))
#     return 1
#
#
# def test_one():
#     assert api_v1() == 1


# import warnings
#
#
# def api_v1():
#     warnings.warn(UserWarning("qqqq"))
#     return 1
#
#
# @pytest.mark.filterwarnings("ignore: qqqq")
# def test_one():
#     assert api_v1() == 1

# #xfail
# xfail = pytest.mark.xfail
#
#
# @xfail
# def test_hello():
#     assert 0
#
#
# @xfail(run=False)
# def test_hello2():
#     assert 0
#
#
# @xfail("hasattr(os, 'sep')")
# def test_hello3():
#     assert 0
#
#
# @xfail(reason="bug 110")
# def test_hello4():
#     assert 0
#
#
# @xfail('pytest.__version__[0] != "17"')
# def test_hello5():
#     assert 0
#
#
# def test_hello6():
#     pytest.xfail("reason")
#
#
# @xfail(raises=IndexError)
# def test_hello7():
#     x = []
#     x[1] = 1


# @pytest.mark.parametrize(
#     ("n", "expected"),
#     [
#         (1, 2),
#         pytest.param(1, 0, marks=pytest.mark.xfail),
#         pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
#         (2, 3),
#         (3, 4),
#         (4, 5),
#         pytest.param(
#             10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0),
#                                              reason="py2k")
#         ),
#     ],
# )
# def test_increment(n, expected):
#     assert n + 1 == expected

# 多组参数化测试
# @pytest.mark.parametrize("test_input,expected",
#                          [("3+5", 8),
#                           ("2+4", 6),
#                           ("6*9", 42)
#                           ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

# 利用xfail进行跳错
# @pytest.mark.parametrize("test_input,expected",
#                          [("3+5", 8),
#                           ("2+4", 6),
#                           pytest.param("6*9", 42, marks=pytest.mark.xfail)
#                           ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

# 故障设置
# @pytest.mark.parametrize("i", range(15))
# def test_num(i):
#     if i in (1, 13):
#        pytest.fail("bad luck")

# 浮点数想加用pytest.approx进行判断
# def test_sum():
#     assert 0.1 + 0.2 == pytest.approx(0.3)

# @attrs
# class Foo(object):
#     a = attrib(default=0)
#     b = attrib(default='Hello world')
#     print(a)
#     print(b)
# c = Foo()
# print(c.a)
# print(c.b)











