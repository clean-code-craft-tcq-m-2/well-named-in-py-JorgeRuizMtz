import request_a_number
import request_two_colors
import get_pair_number_from_color
import test_pair_to_number
import get_color_from_pair_number
import test_number_to_pair
import Menu
import Fail

def second_menu(des):
  if des == 1:
    major,minor = request_two_colors.request_two_colors()
    result = get_pair_number_from_color.get_pair_number_from_color(major, minor)
    test_pair_to_number.test_pair_to_number(major, minor, result)
    print("The corresponding Number for your colors is: ",result)
    print("Test Done")
    input("Press Enter to continue")
    Menu.Menu()

  elif  des == 2:
    num = request_a_number.request_a_number()
    first_color, second_color = get_color_from_pair_number.get_color_from_pair_number(int(num))
    test_number_to_pair.test_number_to_pair(int(num), first_color, second_color) 
    print("The corresponding colors are:\n","Major Color:",first_color,"\n","Minor Color:",second_color)
    print("Test Done")
    input("Press Enter to continue")
    Menu.Menu()
  else:
    Fail.Fail()
    Menu.Menu()