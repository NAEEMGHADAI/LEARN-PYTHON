# Function to convert decimal number
# to binary using recursion


def DecimalToBinary1(num):

    if num > 1:
        DecimalToBinary1(num // 2)
    ans = num % 2
    print(ans, end=' ')


# decimal value
num = int(input('Enter no.\t'))

# Calling function
DecimalToBinary1(num)

# Function to convert decimal number to binary after decimal place


def DecimalToBinary(number):
    n, num, i = 0, 0, 0
    for i in range(1, 6):
        n = number * 2
        num = int(n)
        print(num, end=' ')
        number = n - num
        i = i+1


# input
n = float(input('\nEnter no. after decimal place:\t'))

# calling function
DecimalToBinary(n)
