from PIL import Image
import numpy
from cv2 import imwrite

def get_pixels(img: Image, img_lines: int, img_columns: int) -> list:  
    img_matrix = list(img.getdata())
    # converte a lista anterior para uma lista 2D:
    img_matrix = [img_matrix[offset: offset + img_columns] for offset in range(0, img_columns*img_lines, img_columns)]

    return img_matrix

def import_image(file_path: str) -> Image:
  return Image.open(file_path)

def export_image(matrix: list, name: str) -> bool:
  filename = './export/' + name + '.png'

  try:
    imwrite(filename, numpy.array(matrix))
  except:
    return False
  return True
