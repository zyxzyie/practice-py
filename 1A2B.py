import random as rd

answer = rd.sample("123456789", 4)  # 隨機抽取 4 位數
iswin = False  # flag

while not iswin:
  user_input = list(input("輸入 4 個不同的數字: (若想結束遊戲請輸入0000)"))
  
  # check A: 相同數字、相同位置
  a = 0
  for i in range(4):
    if answer[i] == user_input[i]:
      a = a + 1
  
  # check B: 相同數字、不同位置
  b = 0
  for i in range(4):
    if user_input[i] in answer and user_input[i] != answer[i]:
      b = b + 1
  
  print(f"{a}A{b}B")  # 顯示目前結果
  
  if a == 4:
    print("你答對了! ")
    iswin = True
  
  if user_input == ["0"] * 4:
    print(f"答案是: {answer}")
    break
