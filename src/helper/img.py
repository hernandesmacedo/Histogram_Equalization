import numpy
from cv2 import imread

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
