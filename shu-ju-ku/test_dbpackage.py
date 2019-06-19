# coding:utf-8

import pytest
from DatabasePackage import DbUser


def test_insert():
    db = DbUser()
    user_info = {'name': 'zhangsan', 'age': 18, 'job': 'student'}
    db.insert(user_info)
    result = db.get('zhangsan')
    assert result == user_info

def test_get_exist():
    name = 'zhangsan'
    db = DbUser()
    user_info = {'name': 'zhangsan', 'age': 18, 'job': 'student'}
    db.insert(user_info)
    result = db.get(name)
    assert result == user_info

def test_get_not_exist():
    name = 'lisi'
    db = DbUser()
    result = db.get(name)
    assert result == {}


def test_update_exist():
    db = DbUser()
    user_info = {'name': 'zhangsan', 'age': 18, 'job': 'student'}
    db.insert(user_info)
    name = 'zhangsan'
    data = {'age': 23}
    db.update(name, data)
    result = db.get(name)
    for key, value in data.items():
        assert result[key] == value



def test_update_not_exist():
    db = DbUser()
    name = 'lisi'
    data = {'age': 23}
    with pytest.raises(ValueError):
        db.update(name, data)

def test_delete_exist():
    db = DbUser()
    user_info = {'name': 'zhangsan', 'age': 18, 'job': 'student'}
    db.insert(user_info)

    name = 'zhangsan'
    db.delete(name)
    result1 = db.get(name)
    assert result1 == {}

def test_delete_not_exist():
    db = DbUser()
    name = 'lisi'
    with pytest.raises(ValueError):
        db.delete(name)












