if __name__ == "__main__":
  print("Choose your action? 1 = '+', 2 = '-', 3 = '*', 4 = '/', 5 = '>', 6 = '<=', 7 = '<', 8 = '<=' ")
  x = int(input())
  
  print("Write number 1?")
  num1 = int(input())
  
  print("Write number 2?")
  num2 = int(input())
  if x==1: 
    print("Answer: " + str(num1+num2))
  if x==2:
    print("Answer: " + str(num1-num2))
  if x==3: 
    print("Answer: " + str(num1*num2))
  if x==4:
    if num2!=0:
      print("Answer: " + str(num1/num2))
    else:
      print("Answer: 0")
  if x==5:
    if num1>num2:
      print("True")
    else:
      print("False")
  if x==6:
    if num1<num2:
      print("True")
    else:
      print("False")
  if x==7:
    if num1>=num2:
      print("True")
    else:
      print("False")
  if x==8:
    if num1<=num2:
      print("True")
    else:
      print("False")
  