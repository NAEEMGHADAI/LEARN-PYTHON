class Shape():
    def __init__(self):
        super().__init__()
        self.result

    def area():
        pass

    def printResult():
        print(self.result)
    '''def var(self):
        l = int(input("ENTER LENGTH"))
        b = int(input("ENTER BREADTH"))
        h = int(input("ENTER HEIGHT"))
        r = float(input("ENTER THE RADIUS"))'''


class Rectangle(Shape):
    l = int(input("ENTER LENGTH"))
    b = int(input("ENTER BREADTH"))

    def Area(self):
        super.result = self.l * self.b
        print('Area of Rectangle: ', Area)


class Triangle(Shape):

    h = int(input("ENTER HEIGHT"))

    def Area():
        Area = 0.5 * self.b * self.h
        print("Area of Triangle:", Area)


class Circle(Shape):
    r = float(input("ENTER THE RADIUS"))

    def Area(self):
        Area = 3.14 * self.r * self.r
        print("Area of a circle is: ", Area)


rec = Rectangle()
rec.Area()
rec.printResult()

tir = Triangle()
tir.Area()

cir = Circle()
cir.Area()
