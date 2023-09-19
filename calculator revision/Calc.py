

#-------------------------------------

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

import math
menu = ["Addition", "Subtraction", "Multiply", "Divide"]

while True:
    pick = menuLoad(menu)

    if pick == 0:
        print("See you later")
        break

    elif pick == 99:
        continue

    else:
        num1 = int(input("Enter FIRST number: "))
        num2 = int(input("Enter SECOND number: "))

        if num1.isnumeric() and num2.isnumeric():
            num1 = int(num1)
            num2 = int(num2)

        if pick == 1:
            ans = plus(num1, num2)
            sym = '+'

        elif pick == 2:
            ans = minus(num1, num2)
            sym = '-'

        elif pick == 3:
            ans = multiply(num1, num2)
            sym = '*'

        else:
            if pick == 4:
                ans = divide(num1, num2)
                sym = '/'

        print(f"{num1} {sym} {num2} = {ans}")
