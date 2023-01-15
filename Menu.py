import second_menu

def Menu():

  print("Welcome to 25-pair color code System.")
  print("Please, Select an option \n")
  print("1.- Get a number from Two colors")
  print("2.- Get Two colors from a number\n")
  option = input()
  second_menu.second_menu(int(option))
