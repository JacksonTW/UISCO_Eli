a = b = c = d = e = 0
n = 1
inscore = total = 0
avg = 0.0

a = int(input("輸入第1個數值: "))
b = int(input("輸入第2個數值: "))
c = int(input("輸入第3個數值: "))
d = int(input("輸入第4個數值: "))
e = int(input("輸入第5個數值: "))

total = a+b+c+d+e    
avg = total/5

print("\n\n\n第1個數值：" ,a)
print("第2個數值：" ,b)
print("第3個數值：" ,c)
print("第4個數值：" ,d)
print("第5個數值：" ,e)

print("總和 : %d\n平均數: %d"%(total,avg))
