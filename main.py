#==========[Local Libraries]==========
#-----[Functionality]-----
from src.helper.img import get_pixels
from src.h_equalization.equalization import *

#-----[Terminal Interface]-----
import src.cli.menu as menu

#==========[Main Function]==========
def main():
  img_original = menu.load()
  img_columns, img_lines = img_original.size

  while True:
    selection = menu.home()

    if selection == 0:
      break

    elif selection == 1:
      gray_scale_img = to_gray_scale(img_original)
      gray_img_matrix = get_pixels( gray_scale_img, img_lines, img_columns )
      
      nk = get_histogram(gray_img_matrix, img_lines, img_columns)
      pr_rk = get_pr_rk(nk)
      frequencia = get_freq(pr_rk)
      eq = get_eq(frequencia)
      new_rk = get_new_rk(eq)
      new_img = equalize(gray_img_matrix, new_rk, img_lines, img_columns)

    elif selection == 2:
      menu.export(new_img)

#==========[Script Initializer]==========
if __name__ == "__main__":
  main()
