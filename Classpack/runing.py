# coding:utf-8

class Person(object):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print('我的名字叫{}体重是{}'.format(self.name, self.weight))

    def eat(self):
        self.weight += 1
        print('我的名字叫{}体重是{}'.format(self.name, self.weight))

xiaoming = Person('小明', 45)
xiaoming.run()
xiaoming.eat()

tom = Person('tom',55)
tom.eat()
tom.run()











