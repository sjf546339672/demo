# coding:utf-8

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
print("open successfilly")
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')

print "Table created successfully";


c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

c.execute("UPDATE COMPANY SET SALARY=88888 where id=1")
c.execute("UPDATE COMPANY SET SALARY='{}',NAME='{}' WHERE ID='{}'".format(1111111,'SJF',1))
# c.execute("DELETE FROM COMPANY WHERE id=2")

conn.commit()
print("Recoreds created successfully")

curssor = c.execute("SELECT id, name, address, salary  from COMPANY")
for i in curssor:
    print("ID = ", i[0])
    print("NAME = ", i[1])
    print("ADDRESS = ", i[2])
    print("SALARY = ", i[3])
print("Operation done successfully")
conn.close()





