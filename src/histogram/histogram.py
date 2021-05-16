class Histogram:
  def __init__(self, matrix: list) -> None:
    self.red = [0] * 256
    self.green = [0] * 256
    self.blue = [0] * 256
    
    self.__extract_intensity(matrix)

  def __extract_intensity(self, matrix: list) -> None:
    width, height = len(matrix[0]), len(matrix)

    for y in range(height):
      for x in range(width):
        pixel = matrix[y][x]

        self.red[pixel[0]] += 1
        self.green[pixel[1]] += 1
        self.blue[pixel[2]] += 1

  def basic(self, pixel: list) -> list:
    return [
      self.red[pixel[0]],
      self.green[pixel[1]],
      self.blue[pixel[2]]
    ]
