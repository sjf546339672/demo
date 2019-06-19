# coding:utf-8

import sqlite3
class DbUser(object):


    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE USER
                  (NAME           TEXT    NOT NULL,
                   AGE            INT     NOT NULL,
                   JOB           TEXT    NOT NULL);

                      ''')


    def insert(self, data):
        self.c.execute("INSERT INTO USER (NAME, AGE, JOB) VALUES ('{}', {}, '{}' )".format(data['name'], data['age'], data['job']))
        self.conn.commit()

    def get(self, name):
        getdata = self.c.execute("SELECT name, age, job  from USER WHERE name = '{}'".format(name))
        tuple_data = getdata.fetchone()
        if tuple_data:
            return {'name':tuple_data[0], 'age':tuple_data[1], 'job':tuple_data[2]}
        else:
            return {}

    def update(self, name, data):
        get_data_one = self.get(name)
        if get_data_one:
            query = ["{}='{}'".format(key, value) for key, value in data.items()]
            self.c.execute("UPDATE USER  SET {} where name='{}'".format(','.join(query), name))
        else:
            raise ValueError('User {} not found'.format(name))

    def delete(self, name):
        data_one = self.get(name)
        if data_one:
            self.c.execute("DELETE FROM USER WHERE name='{}'".format(name))
        else:
            raise ValueError('User {} not found'.format(name))


a = DbUser()
a.insert({'name': 'zhangsan', 'age': 18, 'job': 'student'})
a.get('zhangsan')
a.update('zhangsan',{'age': 48, 'job':'English'})
# a.delete('zhangsan')
result = a.get('zhangsan')
print(result)















