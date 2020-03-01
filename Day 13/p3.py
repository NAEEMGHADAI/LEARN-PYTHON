class India():
    def __init__(self):
        print("Object of type India created. I am saying from a constructor 1")

    def capital(self):
        print("New delhi is the capital of India")

    def language(self):
        print("Hindi and English is the native")


class USA():
    def __init__(self):
        print("Object of type India created. I am saying from a constructor 2")

    def capital(self):
        print("Washington,D.C is the Capital of America")

    def language(self):
        print("English is the native")


obj_ind = India()
obj_usa = USA()

ls = []
ls.append(obj_ind)
ls.append(obj_usa)

for country in ls:
    country.capital()
    country.language()
