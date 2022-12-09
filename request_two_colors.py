import os, Fail
from Colors import MAJOR_COLORS, MINOR_COLORS
def request_two_colors():
  os.system("cls") 
  print("Introduce the first color:")
  for i in range(len(MAJOR_COLORS)):
    print(MAJOR_COLORS[i])
  color1 = input()
  os.system("cls")
  if color1 in MAJOR_COLORS:
    indexcol1 = MAJOR_COLORS.index(color1)
    print("Your fist color is",MAJOR_COLORS[indexcol1])
  elif color1 not in MAJOR_COLORS:
    Fail.Fail()
  os.system("cls")
  print("Introduce the second color:")
  for i in range(len(MINOR_COLORS)):
    print(MINOR_COLORS[i])
  color2 = input()
  os.system("cls")
  if color2 in MINOR_COLORS:
    indexcol2 = MINOR_COLORS.index(color2)
    print("Your second color is",MINOR_COLORS[indexcol2])
  elif color2 not in MINOR_COLORS:
    Fail.Fail()
  os.system("cls")
  print("Your First color: ", MAJOR_COLORS[indexcol1],'\n',"Your Secong color: ", MINOR_COLORS[indexcol2])
  return color1, color2
