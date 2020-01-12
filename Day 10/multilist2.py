students = [[1, 'NAEEM', 6000],
            [2, 'AIMAN', 6500],
            [3, 'SALIK', 7000]]

for s in students:
    for i in s:
        print(i)


students = [[1, 'NAEEM', 6000],
            14,
            [3, 'SALIK', 7000],
            'TEST']

for s in students:

    if (isinstance(s, list)):
        print('I FOUND A LIST')
        for i in s:
            print(i, end=" ")
    else:
        print()
        print('NOT A LIST')
        print(s)
