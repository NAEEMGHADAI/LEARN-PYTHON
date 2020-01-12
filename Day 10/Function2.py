
students = [[1, 'NAEEM', 6000],
            14,
            [3, 'SALIK', 7000],
            'TEST']


def printme(ls):

    for s in students:

        if (isinstance(s, list)):
            print('I FOUND A LIST')
            for i in s:
                print(i, end=" ")
        else:
            print()
            print('NOT A LIST')
            print(s)


printme(students)
