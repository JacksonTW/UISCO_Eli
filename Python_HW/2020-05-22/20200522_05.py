import random
count =1
randList = []
tempList = []

for i in range(0, 50):
    tempList.append(0)
while count < 6:
    n = random.randint(1, 49)
    if tempList[n] == 0:
        randList.append(n)
        tempList[n] = 1
        count = count + 1
randList.sort()
print(randList)