hoeveelRepeat = input("Hoeveel keer wil je de fibonacci reeks laten herhalen? ")

def fibonacci(Position):
    previous = 1
    current = 0
    for i in range(Position):
        next = previous + current
        print(next)
        # print(previous/current)
        previous = current
        current = next
fibonacci(int(hoeveelRepeat))
