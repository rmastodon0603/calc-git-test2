import datetime
import os.path
if __name__ == "__main__":
  #save_path = 'C:/Documents/'
  #completeName = os.path.join(save_path, "log.txt")   
  file = open("log.txt", "w")
  dt_now = datetime.datetime.now()
  file.write("[ACTION] "+ str(dt_now) + " : User log in app" + "\n")
  history = "Your History of operations: \n"
  x = int
  while (x!=0):
    print("Choose your action? 0 = 'exit app', 1 = '+', 2 = '-', 3 = '*', 4 = '/', 5 = '>', 6 = '<=', 7 = '<', 8 = '<=', 9 = 'factorial', 10 = 'history of operations' ")
    dt_now = datetime.datetime.now()
    x = int(input())
    if x==0:
      break
    if x==10:
      print(history)
      dt_now = datetime.datetime.now()
      file.write("[ACTION] "+ str(dt_now) + " : User get his history in app" + "\n")
      continue
    dt_now = datetime.datetime.now()
    file.write("[ACTION] "+ str(dt_now) + " : User choose func in app" + "\n")
    print("Write number 1?")
    num1 = int(input())
    dt_now = datetime.datetime.now()
    file.write("[ACTION] "+ str(dt_now) + " : User write num1 in app" + "\n")
    
    print("Write number 2?")
    dt_now = datetime.datetime.now()
    file.write("[ACTION] "+ str(dt_now) + " : User write num2 in app" + "\n")
    num2 = int(input())
    if x==1: 
      print("Answer: " + str(num1+num2))
      history = history + "Your operation was '+'\n"
      dt_now = datetime.datetime.now()
      file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==2:
      print("Answer: " + str(num1-num2))
      history = history + "Your operation was '-'\n"
      dt_now = datetime.datetime.now()
      file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==3: 
      print("Answer: " + str(num1*num2))
      history = history + "Your operation was '*'\n"
      dt_now = datetime.datetime.now()
      file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==4:
      if num2!=0:
        print("Answer: " + str(num1/num2))
        history = history + "Your operation was '/'\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
      else:
        print("Answer: 0")
        history = history + "Your operation was '/'\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==5:
      if num1>num2:
        print("True")
        history = history + "Your operation was '>'\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
      else:
        print("False")
        history = history + "Your operation was '>'\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==6:
      if num1<num2:
        print("True")
        history = history + "Your operation was '<'\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
      else:
        print("False")
        history = history + "Your operation was '<'\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==7:
      if num1>=num2:
        print("True")
        history = history + "Your operation was '>='\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
      else:
        print("False")
        history = history + "Your operation was '>='\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==8:
      if num1<=num2:
        print("True")
        history = history + "Your operation was '<='\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
      else:
        print("False")
        history = history + "Your operation was '<='\n"
        dt_now = datetime.datetime.now()
        file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
    if x==9:
      factorial = 1
      for i in range(2, num1+1):
        factorial *= i
      print(factorial)
      history = history + "Your operation was 'factorial'\n"
      dt_now = datetime.datetime.now()
      file.write("[ACTION] "+ str(dt_now) + " : User get answer in app" + "\n")
  
  dt_now = datetime.datetime.now()
  file.write("[ACTION] "+ str(dt_now) + " : User logour from app" + "\n")
  file.close()
  print("Goodbey\n")

  