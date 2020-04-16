season = int(input('清輸入月份(1~12)，輸入 0 退出：'))
while season != 0 :
  #season = int(input('清輸入月份(1~12)，輸入 0 則退出：'))
  if  season > 0 and season <= 3 :
      print(' %d月是「春天」'%season)
      #break
  elif season > 3 and season <= 6 :
      print(' %d月是「夏天」'%season)
      #break
  elif season > 6 and season <= 9 :
      print(' %d月是「秋天」'%season)
      #break
  elif season > 9 and season <= 12 :
      print(' %d月是「冬天」'%season)
      #break
  else :
      print(' ※ 請輸入有效的月份！！！')
  season = int(input('清輸入月份(1~12)，輸入 0 則退出：'))
print(' ※ 離開.')