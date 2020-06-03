import random

randList = [0, 0, 0, 0, 0]
sum = 0
for i in range(6):
    randList[i - 1] = random.randint(1, 100)
    sum = sum + randList[i - 1]
#    print(randList[i - 1])
#    print('-----')
randList.sort()
# print(randList)

print('總和為 %d' % sum)
print('最大值為 %d' % randList[4])
print('最小值為 %d' % randList[0])
