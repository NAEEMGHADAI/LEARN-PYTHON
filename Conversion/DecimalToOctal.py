# Function to convert decimal number
# to binary using recursion


def DecimalToOctal1(num):

    if num > 1:
        DecimalToOctal1(num // 8)
    ans = num % 8
    print(ans, end=' ')


# decimal value
num = int(input('Enter no.\t'))

# Calling function
DecimalToOctal1(num)

# Function to convert decimal number after the decimal place


def DecimalToOctal(number):
    n, num, i = 0, 0, 0
    for i in range(1, 6):
        n = number * 8
        num = int(n)
        print(num, end=' ')
        number = n - num
        i = i+1


# input
n = float(input('\nEnter no. after decimal place:\t'))

# calling function
DecimalToOctal(n)
