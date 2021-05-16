import numpy
from pathlib import Path
from cv2 import imread, imwrite

def get_pixels(img: numpy.ndarray) -> list:
  width, height = len(img[0]), len(img)
  pixels = []

  for y in range(height):
    new_line = []
    for x in range(width):
      new_line.append(img[y][x].tolist())
    pixels.append(new_line)

  return pixels

def import_image(file_path: str):
  return imread(file_path)

def export_image(matrix: list, name: str) -> bool:
  Path('./export/').mkdir(exist_ok=True)
  filename = './export/' + name + '.png'

  try:
    imwrite(filename, numpy.array(matrix))
  except:
    return False
  return True
