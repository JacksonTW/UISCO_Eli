num = 1
sum = 0
count = 1
#for i in range(1, 101):
while num < 101:
    #print("---------")
    #print(num)
    a = (num % 7)
    #print(a)
    #print("---------")
    if (a != 0):
        sum = sum + num
        num = num + 1
    else :
        num = num + 1
    #print(sum)
    #print(num)
    #print('Next Round')
print('總和為 %d '%sum)

