import random
randList = [0,0,0,0,0]
sum = 0
max = 0
min = 0
for i in range(1,6):
    randList[i-1] = random.randint(1, 100)
    sum = sum + randList[i-1]
randList.sort()
#print(randList)

print("總合為 %d ,最大值為%d ,最小值為%d" % (sum,randList[0],randList[4]))

