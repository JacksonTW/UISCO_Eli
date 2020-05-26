sum = 0
num = 0
a = int((198 / 3))
for i in range(1, (a + 1)):
    #print("-----")
    #print("第 %d 回" % i)
    #print(num)
    #print("-----")
    num = num + 3
    #print("此數為%d"%num)
    sum = sum + num
    #print("總和為%d" % sum)

print("總和為 %d" % sum)