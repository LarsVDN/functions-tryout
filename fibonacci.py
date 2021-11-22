def fuckFibonacci(Position):
    previous = 1
    current = 1
    for i in range(Position):
        fibonacci = previous + current
        print(fibonacci)
        previous = current
        current = fibonacci
fuckFibonacci(100)
