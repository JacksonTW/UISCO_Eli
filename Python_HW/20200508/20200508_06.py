import random


def main():
    a = 0
    CompareTempMax = 0  # 用來存去當前較大的數字
    CompareTempMin = 1000  # 用來存取當前較小的數字
    for i in range(1, 51):
        a = random.randint(1, 1000)
        if a > CompareTempMax:
            CompareTempMax = a
        elif a < CompareTempMin:
            CompareTempMin = a
        print("第 %d 個數字： " % i, a)
    print("*************************")
    print("最大的數字：", CompareTempMax)
    print("最小的數字：", CompareTempMin)


main()
