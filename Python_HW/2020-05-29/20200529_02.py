import random

randList = [None] * 6
sum = 0

for i in range(1, 7):
    randList[i - 1] = random.randint(1, 100)

sum = randList[1] + randList[2]
print(randList)
print(sum)
