class MyClass:
    '''A SIMPLE CLASS'''
    i = 12345

    def __init__(self):
        self.data = [1, 2, 3]

    def f(self):
        return 'hello world'


obj = MyClass()

obj.i = 100
print(obj.i)
print(MyClass.i)

obj1 = MyClass()
obj1.i = 101
print(obj1.i)

print(MyClass)
result = obj.f()
print(result)

print(obj.data)
