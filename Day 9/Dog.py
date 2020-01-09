class Dog:
    kind = 'German Shepherd'

    def __init__(self, name):
        self.name = name


d = Dog('Fido')
e = Dog('Bull')

print(d.name)
print(d.kind)

d.kind = 'Elcician'
print(d.kind)
print(e.kind)
