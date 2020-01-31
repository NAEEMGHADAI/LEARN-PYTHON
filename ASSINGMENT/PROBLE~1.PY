number = (input('ENTER YOUR MOBILE NUMBER'))

if (len(number) < 10 or len(number) > 10)and(number[0] != 7 or number[0] != 8 or number[0] != 9):
    print('INVALID NUMBER')
else:
    print('ok')
