import math
from PIL import Image
from aggdraw import Draw, Brush, Pen

def hexagon_generator(edge_length, offset):
  """Generator for coordinates in a hexagon."""
  x, y = offset
  for angle in range(0, 360, 60):
    x += math.cos(math.radians(angle)) * edge_length
    y += math.sin(math.radians(angle)) * edge_length
    yield x
    yield y

def main():
  image = Image.new('RGB', (100, 100), 'white')
  draw = Draw(image)
  hexagon = hexagon_generator(40, offset=(30, 15))
  draw.polygon(list(hexagon), Pen('black'), Brush('red'))
  draw.flush()
  image.show()

class HexagonGenerator(object):
  """Returns a hexagon generator for hexagons of the specified size."""
  def __init__(self, edge_length):
    self.edge_length = edge_length

  @property
  def col_width(self):
    return self.edge_length * 3

  @property
  def row_height(self):
    return math.sin(math.pi / 3) * self.edge_length

  def __call__(self, row, col):
    x = (col + 0.5 * (row % 2)) * self.col_width
    y = row * self.row_height
    for angle in range(0, 360, 60):
      x += math.cos(math.radians(angle)) * self.edge_length
      y += math.sin(math.radians(angle)) * self.edge_length
      yield x
      yield y

def main():
  image = Image.new('RGB', (250, 250), 'white')
  draw = Draw(image)
  hexagon_generator = HexagonGenerator(40)
  for row in range(7):
    color = row * 10, row * 20, row * 30
    for col in range(2):
      hexagon = hexagon_generator(row, col)
      draw.polygon(list(hexagon), Brush(color))
  draw.flush()
  image.show()