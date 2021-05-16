#==========[Local Libraries]==========
#-----[Functionality]-----
from src.helper.img import get_pixels

#-----[Terminal Interface]-----
import src.cli.menu as menu

#==========[Main Function]==========
def main():
  img_original = menu.load()
  img_matrix = get_pixels(img_original)

  while True:
    selection = menu.home()

    if selection == 0:
      break

    elif selection == 1:
      img_matrix = get_pixels(img_original)

    elif selection == 2:
      menu.export(img_matrix)

#==========[Script Initializer]==========
if __name__ == "__main__":
  main()
