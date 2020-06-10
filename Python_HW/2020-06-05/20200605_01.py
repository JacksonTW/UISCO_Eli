column = 5  # 直行
row = 2  # 橫列
arr2List = [[0] * row for _ in range(column)]
# initial array

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

print("排序前：")
print(arr2List)
arr2List.sort(key=lambda x: x[0])
print("排序後:")
print(arr2List)
