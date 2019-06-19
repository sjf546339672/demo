# coding:utf-8

import pytest
import hashlib
import time
from tornado import gen


# def test_passing():
#     # assert(1, 2, 3)==(1, 2, 3)
#     assert(1, 2, 3)==(3, 2, 1)



# import pytest
# def test_raises(connect):
#     with pytest.raises(TypeError) as e:
#         connect('localhost', 6379)
#     exec_msg = e.value.args[0]
#     assert exec_msg == 'port type must be int'




# import pytest
# @pytest.mark.finished    # 给需要进行测试的函数加上一个标注
# def test_func1():
#     assert 1 == 1
#
# @pytest.mark.unfinished
# def test_func2():
#     assert 1 != 1




# @pytest.mark.skip(reason='out-of-date api')   #skip跳过测试
# def test_connect():
#     pass


# xfail 表示遇见的失败
# @pytest.mark.xfail(gen.__version__ < '0.2.0',
#                    reason='not supported until v0.2.0')
# def test_api():
#     id_1 = gen.unique_id()
#     id_2 = gen.unique_id()
#     assert id_1 != id_2



'''   
就是参数化测试，即每组参数都独立执行一次测试。
使用的工具就是 pytest.mark.parametrize(argnames, argvalues)
'''
# @pytest.mark.parametrize('passwd',
#                          ['123456',
#                           'abcdefdfs',
#                           'as52345fasdf4'])
# def test_passed_length(passwd):
#     assert len(passwd) >= 8


#   多个参数进行测试
# @pytest.mark.parametrize('user, passwd',
#                          [pytest.param('jack', 'asdfsjfsd', id='User<Jack>'),
#                           pytest.param('tom', '12312435', id='User<Tom>')
#                          ])
# def test_passwd_md5_id(user, passwd):
#     db = {
#         'jack': 'e8dc4081b13434b45189a720b77b6818',
#         'tom': '1702a132e769a623c1adb78353fc9503'
#     }
#     assert hashlib.md5(passwd.encode()).hexdigest() == db[user]
#



# @pytest.fixture()
# def postcode():
#     return '010'
#
# def test_postcode(postcode):
#     assert  postcode == '010'



# 预处理和后处理
# @pytest.fixture()
# def db():
#     print('Connection successful')
#     yield
#     print('Connection closed')
#
#
# def search_user(user_id):
#     d = {
#         '010':'xiaoming'
#     }
#     return d[user_id]
#
# def test_search(db):
#     assert search_user('010') == 'xiaoming'



#  固件自动测试
# DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#
#
# @pytest.fixture(scope='session', autouse=True)
# def timer_session_scope():
#     start = time.time()
#     print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))
#
#     yield
#
#     finished = time.time()
#     print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
#     print('Total time cost: {:.3f}s'.format(finished - start))
#
#
# @pytest.fixture(autouse=True)
# def timer_function_scope():
#     start = time.time()
#     yield
#     print(' Time cost: {:.3f}s'.format(time.time() - start))
#
# def test_1():
#     time.sleep(1)
#
#
# def test_2():
#     time.sleep(2)


# 重命名固件名
# @pytest.fixture(name='age')
# def calculate_average_age():
#     return 28
#
#
# def test_age(age):
#     assert age == 28



# def test_tmpdir(tmpdir):
#     a_dir = tmpdir.mkdir('mytmpdir')
#     a_file = a_dir.join('tmpfile.txt')
#     a_file.write('hello, pytest')
#     assert  a_file.read() == 'hello, pytest!'



# @pytest.fixture(scope='module')
# def my_tmpdir_factory(tmpdir_factory):
#     a_dir = tmpdir_factory.mktemp('mytmpdir')
#     a_file = a_dir.join('tmpfile.txt')
#     a_file.write('hello, pytest!')
#     return a_file





















