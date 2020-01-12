# Function without parameters and no return type


def hello():
    print("WELCOME TO VISUAL LABS")

# function call
# hello()


h = hello
h()

'''f = h
f()

print(f()) '''

# Function without parameters and return type


def hello1():
    print("WELCOME TO VISUAL LABS")
    return 'Your Bonus is Rs 1000'


h = hello1
result = hello1()

print(result)

# Function with  parameters and return type


def add(a, b):
    result = a + b
    return result


r = add(5, 7)
print(r)
