class Person:
    count = 0

    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        Person.count = Person.count + 1


    def set_name(self,name):
        self.name=name

    def set_age(self,age):
        self.age=age

    def set_city(self,city):
        self.city=city

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_city(self):
        return self.city




       


