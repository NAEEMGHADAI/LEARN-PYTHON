# Base Class
class Person(object):
    def __init__(self):
        # super().__init__()
        self.avgLifeSpan = 60
        self.food = []
        self.age = 0


class Employee(Person):
    def __init__(self, name, sal, dept):
        super().__init__()
        self.name = name
        self.dept = dept
        self.sal = sal

    def DisplayInfo(self):
        print("AVG LIFE SPAN: ", self.avgLifeSpan)
        print("NAME: ", self.name)
        print("SAL: ", self.sal)
        print("DEPT: ", self.dept)


#faraz = Person()
#
naeem = Employee("ghadai", 10000, "comp")
naeem.DisplayInfo()
