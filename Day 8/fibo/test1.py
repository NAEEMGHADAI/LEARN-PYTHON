while True:
    try:
        x = int(input('ENTER A NUMBER: '))
        break
    except ValueError:
        print("oops")
