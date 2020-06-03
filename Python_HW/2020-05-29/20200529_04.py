import random

randList = [None] * 8

for i in range(1, 9):
    randList[i - 1] = random.randint(1, 100)

# print(randList)
print(randList[1], randList[2], randList[3], randList[4])
