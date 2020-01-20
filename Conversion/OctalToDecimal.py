# function for octal no. at decimal place
def OctalToDecimal(octal):

    octal1 = octal
    decimal, i, n = 0, 0, 0
    while(octal != 0):
        dec = octal % 10
        decimal = decimal + dec * (8**i)
        octal = octal//10
        i += 1
    print(decimal)

# function for octal no. at fractional place


def OctalToDecimal1(octal1):
    # Python Program to Reverse a Number using While loop

    Reverse = 0
    while(octal1 > 0):
        Reminder = octal1 % 10
        Reverse = (Reverse * 10) + Reminder
        octal1 = octal1 // 10

    decimal, i, n = 0, 1, 0
    while(Reverse != 0):
        dec = Reverse % 10
        decimal = decimal + dec * (8**-i)
        Reverse = Reverse//10
        i += 1
    print(decimal)

# taking value of octal no. at decimal place


octal = int(input("Enter the octal no."))

# function call
OctalToDecimal(octal)

# taking value of octal no. after fraction place
octal1 = float(input("Enter the octal no. after the decimal place"))

# function call
OctalToDecimal1(octal1)
