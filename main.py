#==========[Local Libraries]==========
#-----[Functionality]-----
from src.histogram.histogram import Histogram
from src.helper.img import get_pixels, import_image

#-----[Terminal]-----
from src.helper.histogram import print_basic

#==========[Main Function]==========

def main():
  img_original = import_image('./sample/color_test.png')
  img_matrix = get_pixels(img_original)

  test = Histogram(img_matrix)
  print_basic(test.basic(img_matrix[0][0]))


#==========[Script Initializer]==========
if __name__ == "__main__":
  main()
