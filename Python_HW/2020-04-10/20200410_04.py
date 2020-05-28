pay_money = int(input('請輸入購物金額(輸入 -1 離開)：'))
while pay_money != -1:
  if pay_money >= 5000 and pay_money < 15000:
      total = (pay_money)*0.95
      print(' 實際付款金額為 $ %.2f 元'%total)
  elif pay_money >= 15000 and pay_money < 25000:
      total = (pay_money)*0.9
      print(' 實際付款金額為 $ %.2f 元'%total)
  elif pay_money >= 25000 and pay_money < 35000:
      total = (pay_money)*0.85
      print(' 實際付款金額為 $ %.2f 元'%total)
  elif pay_money >= 35000 :
      total = (pay_money)*0.8
      print(' 實際付款金額為 $ %.2f 元'%total)
  else:
      print(' 很抱歉未達折扣門檻...')
  pay_money = int(input('請輸入購物金額(輸入 -1 離開)：'))
print(' ※ 離開.')