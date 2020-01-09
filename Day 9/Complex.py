class Complex:
    ''' A COMPLEX FUNCTION '''

    def __init__(self, realp, imagep):
        self.r = realp
        self.i = imagep


x = Complex(3.0, -4.5)
print(x.r)
print(x.i)
