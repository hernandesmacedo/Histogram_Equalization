#==========[Local Libraries]==========
#-----[Functionality]-----
from src.helper.img import get_pixels

#-----[Terminal Interface]-----
import src.cli.menu as menu

#==========[Main Function]==========
from src.histogram.histogram import Histogram
from src.helper.img import import_image

def main():
  img_original = import_image('./sample/color_test.png')
  img_matrix = get_pixels(img_original)

  test = Histogram(img_matrix)
  print(test.red)
#==========[Script Initializer]==========
if __name__ == "__main__":
  main()
