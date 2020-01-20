# function for binary no. at decimal place
def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * (2**i)
        binary = binary//10
        i += 1
    print(decimal)

# function for binary no. at fractional place


def binaryToDecimal1(binary1):
    # Python Program to Reverse a Number using While loop

    Reverse = 0
    while(binary1 > 0):
        Reminder = binary1 % 10
        Reverse = (Reverse * 10) + Reminder
        binary1 = binary1 // 10

    decimal, i, n = 0, 1, 0
    while(Reverse != 0):
        dec = Reverse % 10
        decimal = decimal + dec * (2**-i)
        Reverse = Reverse//10
        i += 1
    print(decimal)


# taking value of binary no. at decimal place
binary = int(input("Enter the binary no."))

# function call
binaryToDecimal(binary)

# taking value of binary no. after fraction place
binary1 = float(input("Enter the binary no. after the decimal place"))

# function call
binaryToDecimal1(binary1)
