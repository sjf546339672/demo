# coding: utf-8

from train_models import Person, School, Session

# s1 = School(id='1', school_name='舒城中学1', class_name='高三一班')
# s2 = School(id='2', school_name='舒城中学2', class_name='高三二班')
# s3 = School(id='3', school_name='舒城中学3', class_name='高三三班')
# s1 = Person(id=1, name='Tom1', age=13)
# s2 = Person(id=2, name='Tom2', age=23)
# s3 = Person(id=3, name='Tom3', age=33)
# s4 = Person(id=4, name='Tom4', age=34)
# Session.add_all([s1, s2, s3, s4])
# Session.commit()

# rows = Session.query(School).first()
# print(rows.id, rows.school_name)

# 查询所
# query_all = Session.query(Person.id, Person.name, Person.age).all()
# print(query_all)

# 条件查询
# query = Session.query(
#     Person.id,
#     Person.name,
#     Person.age).filter(Person.age > 30).all()

# query = Session.query(
#     School.id,
#     School.class_name).filter(School.school_name == "舒城中学").all()
# print(query)






