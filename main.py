import datetime
if __name__ == "__main__":
  print("Choose your action? 1 = '+', 2 = '-', 3 = '*', 4 = '/', 5 = '>', 6 = '<=', 7 = '<', 8 = '<=', 9 = 'factorial' ")
  file = open("log.txt", "w")
  dt_now = datetime.datetime.now()
  file.write(str(dt_now) + " : User log in app" + "\n")
  x = int(input())
  dt_now = datetime.datetime.now()
  file.write(str(dt_now) + " : User choose func in app" + "\n")
  print("Write number 1?")
  num1 = int(input())
  dt_now = datetime.datetime.now()
  file.write(str(dt_now) + " : User write num1 in app" + "\n")
  
  print("Write number 2?")
  dt_now = datetime.datetime.now()
  file.write(str(dt_now) + " : User write num2 in app" + "\n")
  num2 = int(input())
  if x==1: 
    print("Answer: " + str(num1+num2))
    dt_now = datetime.datetime.now()
    file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==2:
    print("Answer: " + str(num1-num2))
    dt_now = datetime.datetime.now()
    file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==3: 
    print("Answer: " + str(num1*num2))
    dt_now = datetime.datetime.now()
    file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==4:
    if num2!=0:
      print("Answer: " + str(num1/num2))
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
    else:
      print("Answer: 0")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==5:
    if num1>num2:
      print("True")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
    else:
      print("False")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==6:
    if num1<num2:
      print("True")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
    else:
      print("False")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==7:
    if num1>=num2:
      print("True")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
    else:
      print("False")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==8:
    if num1<=num2:
      print("True")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
    else:
      print("False")
      dt_now = datetime.datetime.now()
      file.write(str(dt_now) + " : User get answer in app" + "\n")
  if x==9:
    factorial = 1
    for i in range(2, num1+1):
      factorial *= i
    print(factorial)
    dt_now = datetime.datetime.now()
    file.write(str(dt_now) + " : User get answer in app" + "\n")
  file.close()

  