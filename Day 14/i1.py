class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):
    def isEmployee(self):
        return True


class Sport(Employee):
    def cricket(self):
        return ("CRICKET")


naeem = Person("NAEEM")
print(naeem.getName())

ak = Employee("ABDULKADIR")
print(ak.isEmployee())

joks = Sport("ZAKI")
print(joks.cricket())
