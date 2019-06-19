# coding:utf-8
import pytest
from DatabasePackage import DbUser


class TestMethod(object):

    @classmethod
    def setup_class(cls):
        """在类运行之前执行该函数   setup_class 固定的方法"""
        data = [
            {'name': 'zhangsan', 'age': 18, 'job': 'student'},
            {'name': 'lisi', 'age': 18, 'job': 'student'}
        ]
        cls.db = DbUser()        # 初始化数据库
        for i in data:
            cls.db.insert(i)        # 向数据库插入数据

    def test_get_exist(self, get_date):        # 定义测试获取数据函数
        result = self.db.get(get_date['name'])
        assert result == get_date

    @pytest.fixture(params=[{'name': 'wangwu', 'age': 18, 'job': 'student'}])
    def get_name(self, request):        # 获取字典函数
        return request.param            # 获取传入的字典

    def test_get_not_exist(self, get_name):        # 定义测试没有获取到属性值得函数
        result = self.db.get(get_name['name'])    # 获取字典传入的key='name'的值
        assert result == {}

    @pytest.mark.parametrize(argnames="name, data",
                             argvalues=[
                                ('zhangsan', {'age': 18, 'job': 'student'}),
                                ('lisi', {'age': 18})
                             ])
    def test_update_exist(self, name, data):        # 定义测试更新数据库数据函数
        self.db.update(name, data)
        result = self.db.get(name)
        for key, value in data.items():
            assert result[key] == value

    @pytest.mark.parametrize(argnames="name, data",
                             argvalues=[
                                 ('jom', {'age': 18, 'job': 'student'}),
                                 ('Anal', {'age': 18})
                             ])
    def test_update_not_exist(self, name, data):
        """定义测试更新数据库的数据不存在异常处理函数"""
        with pytest.raises(ValueError):
            self.db.update(name, data)

    @pytest.mark.parametrize(argnames="name", argvalues=['zhangsan', 'lisi'])
    def test_delete_exist(self, name):
        """定义测试删除数据函数"""
        self.db.delete(name)
        result1 = self.db.get(name)
        assert result1 == {}

    @pytest.mark.parametrize(argnames="name", argvalues=['TOM', 'BOB'])
    def test_delete_not_exist(self, name):
        """定义测试删除数据不存在函数"""
        with pytest.raises(ValueError):
            self.db.delete(name)

