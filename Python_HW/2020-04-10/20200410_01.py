temp = int(input('請輸入天氣(輸入 200 離開)：'))
while temp <= 150:
    if temp >= 28:
        print('The weather is hot！')
    elif temp < 20:
        print('The weather is cold！')
    else:
        print('The weather is comfortable！')
    temp = int(input('請輸入天氣(輸入 200 則離開)：'))
print(' ※ 離開.')
