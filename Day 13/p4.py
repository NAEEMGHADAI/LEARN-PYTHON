class Bird():
    def __init__(self):
        super().__init__()

    def intro(self):
        print("THERE ARE MANY TYPES OF BIRDS")

    def flight(self):
        print("Some birds can Flight")


class sparrow(Bird):
    def __init__(self):
        super().__init__()

    def flight(self):
        print('sparrow can fly')


class ostrich(Bird):
    def flight(self):
        print('Ostrich cannot fly')


B = Bird()
S = sparrow()
O = ostrich()

B.intro()
B.flight()

S.flight()
S.intro()

O.flight()
O.intro()
