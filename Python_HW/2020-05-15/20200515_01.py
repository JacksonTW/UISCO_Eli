def max(x, y):
    if x > y:
        print("最大值為 %d" % x)
    else:
        print("最大值為 %d" % y)

def main():
    a = int(input("請輸入第一個數： "))
    b = int(input("請輸入第二個數： "))
    max(a, b)
main()
