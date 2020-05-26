age = int(input('請輸入年齡(輸入 -1 離開)：'))

while age >= 0:
  if age >= 0 and age < 7 :
      print(' %d 歲為童年'%age)
  elif age >=7 and age < 18 :
      print(' %d 歲為少年'%age)
  elif age >=18 and age < 41 :
      print(' %d 歲為青年'%age)
  elif age >=41 and age < 66 :
      print(' %d 歲為中年'%age)
  elif age >=66 :
      print(' %d 歲為老年'%age)
  age = int(input('請輸入年齡：'))
print(' ※ 離開.')