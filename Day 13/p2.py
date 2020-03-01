def add(x, y, z=0, v=1):
    return x + y + z + v


def add(x, y, z=5, v=10):
    return x + y + z + v


#add = "efs"

'''py p2.py
Traceback(most recent call last):
  File "p2.py", line 13, in < module >
  print(add(2, 3))  # 20
TypeError: 'str' object is not callable'''

# Driver code
print(add(2, 3))  # 20
print(add(2, 3, 4))  # 19
print(add(2, 3, 4, 5))  # 14
