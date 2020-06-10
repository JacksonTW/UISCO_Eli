column = 5  # 直行
row = 2  # 橫列
arr2List = [[0] * row for _ in range(column)]
arrRowSum = [0]*2
# initial array
sum = 0

arr2List[0][0] = 8
arr2List[0][1] = 20
arr2List[1][0] = 3
arr2List[1][1] = 25
arr2List[2][0] = 1
arr2List[2][1] = 29
arr2List[3][0] = 7
arr2List[3][1] = 33
arr2List[4][0] = 4
arr2List[4][1] = 12

for i in range(2):
    for j in range(5):
        arrRowSum[i] = arrRowSum[i]+arr2List[j][i]

sum = arrRowSum[0]+arrRowSum[1]
print("二維陣列：", arr2List)
print("二維總和：", sum)
