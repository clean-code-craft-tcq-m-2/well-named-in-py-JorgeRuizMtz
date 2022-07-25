import os
import Menu

def Fail(): 
  os.system("cls")
  print("Invalid option, Please try again")
  input("Press Enter to continue\n ")
  Menu.Menu() 