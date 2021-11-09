if __name__ == "__main__":
  print("Choose your action? 1 = '+', 2 = '-', 3 = '*', 4 = '/'")
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
    print("Answer: " + str(num1/num2))
  