import random

randList = [None] * 7

for i in range(1, 8):
    randList[i - 1] = random.randint(1, 100)
randList.sort(reverse=True)

print(randList)
