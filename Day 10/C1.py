class Dog:
    kind = 'bull dog'
    # class variable

    def __init__(self, name):
        print('Instance Created of dog')
        self.name = name


d = Dog('Trump')
print(d.kind)
d.kind = 'German Shepherd'
print(d.kind)
print(d.name)
print(d.name, ' is ', d.kind)
