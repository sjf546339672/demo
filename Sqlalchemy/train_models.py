# coding: utf-8

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()
# 初始化数据库连接
engin = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test1',
                      encoding="utf-8", echo=True, max_overflow=5)


# 定义User对象
class Person(Base):
    # 标的名字
    __tablename__ = 'person'

    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    age = Column(Integer)


# 定义User对象
class School(Base):
    # 标的名字
    __tablename__ = 'school'

    # 表的结构
    id = Column(Integer, primary_key=True)
    school_name = Column(String(32))
    class_name = Column(String(64))


Base.metadata.create_all(engin)

# 创建DBsession类型
Session_class = sessionmaker(bind=engin)

Session = Session_class()

