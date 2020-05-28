def main(a, b):
    star = int(a)
    end = int(b)
    b = a
    for i in range(star, (end+1)):
        print(b)
        b = b + 1
        # print(b)


star = int(input("請輸入起始值： "))
end = int(input("請輸入終止值： "))
main(star, end)
