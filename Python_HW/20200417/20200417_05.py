count = 1
num = 1
#a = int(input("請輸入層數： "))
for i in range(1, 7):
    if i == 1:
        print("%d%d%d%d%d%d" % (i, i+1, i+2, i+3, i+4, i+5))
    elif i == 2:
        print("%d%d%d%d%d" % (i-1, i, i+1, i+2, i+3))
    elif i == 3:
        print("%d%d%d%d" % (i-2, i-1, i, i+1))
    elif i == 4:
        print("%d%d%d" % (i-3, i-2, i-1))
    elif i == 5:
        print("%d%d" % (i-4, i-3))
    elif i == 6:
        print("%d" % (i-5))
    else:
        pass
