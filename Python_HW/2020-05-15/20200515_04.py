def printStar(n):
    for i in range(n):
        print(" "*(n-i), end="")
        print("* "*(i+1))


def main():
    key = int(input("請輸入行數： "))
    printStar(key)


main()
