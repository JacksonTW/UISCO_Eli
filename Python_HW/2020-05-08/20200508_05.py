import random


def main():
    OddCount = 0  # 奇數
    EvenCount = 0  # 偶數
    a = int(0)
    b = int(0)
    for i in range(1, 51):
        a = random.randint(1, 1000)
        b = a % 2
        if b == 0:
            EvenCount += 1
        else:
            OddCount += 1
        print("第 %d 個數字： " % i, a)
    print("*************************")
    print("奇數共 %d 個" % OddCount)
    print("偶數共 %d 個" % EvenCount)


main()
