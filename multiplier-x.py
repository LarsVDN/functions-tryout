def table(x):
    for i in range(1, 11):
        print(x, "x", i, "=", x * i)

def main():
    x = int(input("Van welk getal wilt u de tafel zien? "))
    table(x)

main()
