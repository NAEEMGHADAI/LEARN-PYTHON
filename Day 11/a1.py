def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return ("HELLO WORLD")

    h = g


x = C()

print(x.f(2, 10))

print(x.h())
print(x.g())
