# coding:utf-8

import pytest
from DatabasePackage import DbUser

class TestMethod(object):

    # @pytest.fixture(params=dates)
    # def get_date(self, request):
    #     return request.param


    @classmethod
    def setup_class(cls):
        datas = [{'name': 'zhangsan', 'age': 18, 'job': 'student'}, {'name': 'lisi', 'age': 18, 'job': 'student'}]
        cls.db = DbUser()
        for i in datas:
            cls.db.insert(i)

    def test_get_exist(self, get_date):
        result = self.db.get(get_date['name'])
        assert result == get_date

    dates = [{'name': 'wangwu', 'age': 18, 'job': 'student'}]
    @pytest.fixture(params=dates)
    def get_name(self, request):
        return request.param

    def test_get_not_exist(self, get_name):
        result = self.db.get(get_name['name'])
        assert result == {}


    @pytest.mark.parametrize("name, data", [('zhangsan', {'age': 18, 'job': 'student'}), ('lisi', {'age': 18})])
    def test_update_exist(self, name, data):
        self.db.update(name, data)
        result = self.db.get(name)
        for key, value in data.items():
            assert result[key] == value

    @pytest.mark.parametrize("name, data", [('ttt', {'age': 18, 'job': 'student'}), ('iii', {'age': 18})])
    def test_update_not_exist(self, name, data):
        with pytest.raises(ValueError):
            self.db.update(name, data)



    @pytest.mark.parametrize("name", ['zhangsan', 'lisi'])
    def test_delete_exist(self, name):
        self.db.delete(name)
        result1 = self.db.get(name)
        assert result1 == {}


    @pytest.mark.parametrize("name", ['tt','ttttt'])
    def test_delete_not_exist(self, name):
        with pytest.raises(ValueError):
            self.db.delete(name)





# @pytest.fixture(params=[0, 1], ids=["spam", "ham"])
# def a(request):
#     return request.param
#
# def test_a(a):
#     print(a)




