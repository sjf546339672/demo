# coding:utf-8

from contextlib import contextmanager
import requests
import pytest
import os
import sys
import attr
import datetime
import distutils.spawn
import subprocess
import textwrap

'''
py.test --version               查看版本
py.test --fixtures, --funcargs  查看可用的 fixtures
pytest --markers                查看可用的 markers
py.test -h, --help              命令行和配置文件帮助

# 失败后停止
py.test -x           首次失败后停止执行
py.test --maxfail=2  两次失败之后停止执行

# 调试输出
py.test -l, --showlocals  在 traceback 中显示本地变量
py.test -q, --quiet       静默模式输出
py.test -v, --verbose     输出更详细的信息
py.test -s                捕获输出, 例如显示 print 函数的输出
py.test -r char           显示指定测试类型的额外摘要信息
py.test --tb=style        错误信息输出格式
    - long    默认的traceback信息格式化形式
    - native  标准库格式化形式
    - short   更短的格式
    - line    每个错误一行

# 运行指定 marker 的测试
pytest -m MARKEXPR

# 运行匹配的测试
py.test -k stringexpr

# 失败时调用 PDB
py.test --pdb


'''


'''
pytest-randomly: 测试顺序随机
pytest-xdist: 分布式测试
pytest-cov: 生成测试覆盖率报告
pytest-pep8: 检测代码是否符合 PEP8 规范
pytest-flakes: 检测代码风格
pytest-html: 生成 html 报告
pytest-rerunfailures: 失败重试
pytest-timeout: 超时测试
'''

'''
# 跳过测试 @pytest.mark.skip(reason=None) 

# 满足某个条件时跳过该测试 @pytest.mark.skipif(condition) 

# 预期该测试是失败的 
@pytest.mark.xfail(condition, reason=None, run=True, raises=None, strict=False)

# 参数化测试函数。给测试用例添加参数，供运行时填充到测试中 

# 如果 parametrize 的参数名称与 fixture 名冲突，则会覆盖掉 
fixture @pytest.mark.parametrize(argnames, argvalues) 

# 对给定测试执行给定的 fixtures 

# 这种用法与直接用 fixture 效果相同 

# 只不过不需要把 fixture 名称作为参数放在方法声明当中 
@pytest.mark.usefixtures(fixturename1, fixturename2, ...) 

# 让测试尽早地被执行 @pytest.mark.tryfirst 

# 让测试尽量晚执行 @pytest.mark.trylast

'''

'''
节点信息

获得指定节点的名字，简介，URL 及头像图片的地址。

https://www.v2ex.com/api/nodes/show.json

Method: GET
Authentication: None
接受参数：

name: 节点名（V2EX 的节点名全是半角英文或者数字）
例如：

https://www.v2ex.com/api/nodes/show.json?name=python

接口返回

{
    "id" : 90,
    "name" : "python",
    "url" : "http://www.v2ex.com/go/python",
    "title" : "Python",
    "title_alternative" : "Python",
    "topics" : 7963,
    "stars" : 5138,

        "header" : "这里讨论各种 Python 语言编程话题，也包括 Django，Tornado 等框架的讨论。这里是一个能够帮助你解决实际问题的地方。",


        "footer" : null,

    "created" : 1278683336,
    "avatar_mini" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_mini.png?m=1509941286",
    "avatar_normal" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_normal.png?m=1509941286",
    "avatar_large" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_large.png?m=1509941286"
}


'''


# class TestApi(object):
#     """接口测试"""
#     domain = 'https://www.v2ex.com/'
#
#     def test_node(self):
#         path = 'api/nodes/show.json?name=python'
#         url = self.domain + path
#         res = requests.get(url).json()
#         assert res['id'] == 90
#         assert res['name'] == 'python'


# 具有多个Fixture的间接参数化
# pythonlist = ["python3.5", "python3.6", "python3.7"]
#
#
# @pytest.fixture(params=pythonlist)
# def python1(request, tmpdir):
#     pickle_file = tmpdir.join('data.pickle')
#     return Python(request.param, pickle_file)
#
#
# @pytest.fixture(params=pythonlist)
# def python2(request, python1):
#     return Python(request.param, python1.packlefile)
#
#
# class Python:
#     def __init__(self, version, picklefile):
#         self.pythonpath = distutils.spawn.find_executable(version)
#         if not self.pythonpath:
#             pytest.skip("{!r} not found".format(version))
#         self.picklefile = picklefile
#
#     def dumps(self, obj):
#         dumpfile = self.picklefile.dirpath("dump.py")
#         dumpfile.write(
#             textwrap.dedent(
#                 r"""
#                 import pickle
#                 f = open({!r}, 'wb')
#                 s = pickle.dump({!r}, f, protocol=2)
#                 f.close()
#                 """.format(
#                     str(self.picklefile), obj
#                 )
#             )
#         )
#         subprocess.check_call((self.pythonpath, str(dumpfile)))
#
#     def load_and_is_true(self, expression):
#         loadfile = self.picklefile.dirpath("load.py")
#         loadfile.write(
#             textwrap.dedent(
#                 r"""
#                 import pickle
#                 f = open({!r}, 'rb')
#                 obj = pickle.load(f)
#                 f.close()
#                 res = eval({!r})
#                 if not res:
#                     raise SystemExit(1)
#                 """.format(
#                     str(self.picklefile), expression
#                 )
#             )
#         )
#         print(loadfile)
#         subprocess.check_call((self.pythonpath, str(loadfile)))
#
#
# @pytest.mark.parametrize("obj", [42, {}, {1: 3}])
# def test_basic_objects(python1, python2, obj):
#     python1.dumps(obj)
#     python2.load_and_is_true("obj == %s" % obj)


# @pytest.fixture(scope="session")
# def base_mod(request):
#     return pytest.importorskip("base")
#
#
# @pytest.fixture(scope="session", params=["opt1", "opt2"])
# def opt_mod(request):
#     return pytest.importorskip(request.param)
#
#
# def func1():
#     return 1
#
#
# # def func1():
# #     return 1.0001
#
#
# def test_func1(base_mod, opt_mod):
#     assert round(base_mod.func1(), 3) == round(opt_mod.func1(), 3)


# 参数化条件提升
# @contextmanager
# def does_not_raise():
#     """定义一个无操作的上下文管理器"""
#     yield
#
#
# @pytest.mark.parametrize('example_input,expectation',
#                          [(3, does_not_raise()),
#                           (2, does_not_raise()),
#                           (1, does_not_raise()),
#                           (0, pytest.raises(ZeroDivisionError)),
#                           ])
# def test_division(example_input, expectation):
#     with expectation:
#         assert (6 / example_input) is not None


# 使用fixture参数化接口入参
# class TestApiParams(object):
#     domain = 'https://www.v2ex.com/'
#
#     @pytest.fixture(params=['python', 'java', 'go', 'nodejs'])
#     def lang(self, request):
#         return request.param
#
#     def test_node(self, lang):
#         path = 'api/nodes/show.json?name=%s' %(lang)
#         url = self.domain + path
#         res = requests.get(url).json()
#         assert res['name'] == lang
#
#
# class TestApiParams(object):
#     domain = 'https://www.v2ex.com/'
#
#     @pytest.mark.parametrize('subject',
#                              ['python', 'java', 'go', 'nodejs',
#                               pytest.param('jsp', marks=pytest.mark.xfail)
#                               ])
#     def test_node(self, subject):
#         path = 'api/nodes/show.json?name={}'.format(subject)
#         url = self.domain + path
#         res = requests.get(url).json()
#         assert res['name'] == subject
#
#
# class TestApiExpectation(object):
#     domain = 'https://www.v2ex.com/'
#
#     @pytest.mark.parametrize('name, node_id',
#                              [('python', 90),
#                               ('java', 63),
#                               ('go', 375),
#                               ('nodejs', 436),
#                               ])
#     def test_node(self, name, node_id):
#         path = 'api/nodes/show.json?name={}'.format(name)
#         url = self.domain + path
#         res = requests.get(url).json()
#         assert res['name'] == name
#         assert res['id'] == node_id


# @pytest.fixture(params=[1, 2, 3])
# def test_data(request):
#     return request.param
#
#
# def test_not_2(test_data):
#     print('test_data: %s' % test_data)
#     assert test_data != 5


# CONTENT = "content"
#
#
# def test_create_file(tmpdir):
#     p = tmpdir.mkdir("sub").join("hello.txt")
#     p.write("content")
#     assert p.read() == "content"
#     assert len(tmpdir.listdir()) == 1


# def test_needsfiles(tmpdir):
#     print tmpdir
#     return 0















