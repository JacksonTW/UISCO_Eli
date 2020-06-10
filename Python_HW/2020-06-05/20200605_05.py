import random
column = 5  # 直行
row = 2  # 橫列
#arr2List = [[0] * row for _ in range(column)]
# initial array
column = int(input("請輸入需要的直行數： "))
row = int(input("請輸入需要的橫列數： "))

arr2List = [[0] * row for _ in range(column)]

for i in range(column):
    for j in range(row):
        arr2List[i][j] = random.randint(1, 100)

print(arr2List)
