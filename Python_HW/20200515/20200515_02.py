def sum(n):
    a =int(0)
    for i in range(1, n+1):
        a = a + i
    print("總和為 %d"%a)





def main():
    key = int(input("請輸入整數數字："))
    sum(key)

main()