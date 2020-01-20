# Function to convert decimal number
# to binary using recursion


def decimal_to_hexadecimal1(dec):
    decimal = int(dec)

    # Prints equivalent decimal
    print(decimal, " in Hexadecimal : ", hex(decimal))


# decimal value
num = int(input('Enter no.\t'))

# Calling function
decimal_to_hexadecimal1(num)

# Function to convert decimal number to binary after decimal place


def DecimalToHexadecimal(number):
    n, num, i = 0, 0, 0
    for i in range(1, 6):
        n = number * 16
        num = int(n)
        if (num == 10):
            print("A")
        elif (num == 11):
            print("B")
        elif (num == 12):
            print("C")
        elif (num == 13):
            print("D")
        elif (num == 14):
            print("E")
        elif (num == 15):
            print("F")
        else:
            print(num, end=' ')
        number = n - num
        i = i+1


# input
n = float(input('\nEnter no. after decimal place:\t'))

# calling function
DecimalToHexadecimal(n)
