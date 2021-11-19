def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def increment(number):
    return number + 1

def decrement(number):
    return number - 1

print(("10 + 12 ="),addition(10,12))
print(("58 - 34 ="),subtraction(58,34))
print(("6 x 7 ="),multiplication(6,7))
print(("144 : 12 ="),int(division(144,12)))
print(("12 + 1 ="),increment(12))
print(("34 - 1 ="),decrement(34))
