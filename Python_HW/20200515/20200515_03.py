def triArea(x, y):
    area = (x * y)/2
    print("三角形面積：%d" % area)


def main():
    BotEdge = int(input("請輸入三角形底邊長度： "))
    tall = int(input("請輸入三角形高度： "))
    triArea(BotEdge, tall)


main()
