import random

resultList = []
A = 30  # 最小
B = 90  # 最大
count = 5

resultList = random.sample(range(A, B + 1), count)
resultList.sort()
print(resultList)
