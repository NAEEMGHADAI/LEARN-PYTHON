contact = {'Naeem': 9004273149, 'aiman': 934793927,
           'Salik': 8298928923, 'zaki': 898989898}

print(contact)

print(contact['Naeem'])

del contact['aiman']

print(contact)

print(sorted(contact))


for k, v in contact.items():
    print(k, v)

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)


def add(key, value):
    contact[key] = value


add('ahmed', 909089898)
print(contact)
