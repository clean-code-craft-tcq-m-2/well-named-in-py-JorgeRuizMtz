import os
import Fail

def request_a_number():
  
  os.system("cls")
  print("Introduce a number:")
  num1 = input()
  os.system("cls")
  print("Your number is:",num1)
  if int(num1) > 25:
    Fail.Fail()
  elif int(num1) <= 0:
    Fail.Fail()
  else:
    return num1
 
