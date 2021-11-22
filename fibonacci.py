def fuckFibonacci(Position):
    previous = 1
    current = 1
    for i in range(Position):
        fibonacci = previous + current
        print(fibonacci)
        previous = current
        current = fibonacci
<<<<<<< HEAD
fuckFibonacci(100)
=======
fuckFibonacci(1000000)
>>>>>>> 0ee55fee73a57e113f20b462781f187ca62dfc8a
