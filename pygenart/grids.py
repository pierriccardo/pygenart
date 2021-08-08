from PIL import Image, ImageDraw
import numpy as np
from abc import abstractmethod
from pygenart.utils import *
#from aggdraw import Draw, Pen, Brush

class Grid():
    def __init__(self, size, unit, dpi=100, noise='none', noise_value=100):
        self.size = size
        self.w, self.h = size
        self.rows = int(self.w / unit)
        self.cols = int(self.h / unit)
        self.img = Image.new('RGB', size)
        self.draw = ImageDraw.Draw(self.img)

        self.unit = unit
        self.noise = noise
        self.noise_value = noise_value

        self.pixels = self.img.load()
    
    @abstractmethod
    def apply(self):
        pass 

    def noise_gaussian(self, color):
        return tuple([int(np.random.normal(1)*self.noise_value + c) for c in color])
    
    def save(self, path):
        self.img.save(path)



class PixelGrid(Grid):

    def __init__(self, size, unit, dpi=100, noise='none', noise_value=100):
        self.size = size
        self.w, self.h = size
        self.rows = int(self.w / unit)
        self.cols = int(self.h / unit)
        self.img = Image.new('RGB', size)
        self.unit = unit
        self.noise = noise
        self.noise_value = noise_value

        self.pixels = self.img.load()
    
    def apply(self, cmap):

        for row in range(self.rows):
            for col in range(self.cols):
                unit_row, unit_col = row*self.unit, col*self.unit

                for x in range(unit_row, unit_row+self.unit):
                    for y in range(unit_col, unit_col+self.unit):
                        r, g, b = cmap[row, col]

                        if self.noise == 'gaussian':
                            r, g, b, = self.noise_gaussian(cmap[row, col])

                        self.pixels[x, y] = int(r), int(g), int(b)

class HexagonalGrid(Grid):

    def __init__(self, size, unit, dpi=100, noise='gaussian', noise_value='10'):
        super().__init__(size, unit, dpi=dpi, noise=noise, noise_value=noise_value)

    def apply(self, cmap):
        
        hex_gen = HexagonGenerator(self.unit)
        for row in range(self.rows):
            for col in range(self.cols):
                hexagon = hex_gen(row, col)

                self.draw.polygon(list(hexagon), fill=tuple(cmap[row, col]))
        

class HexagonGenerator(object):
    """Returns a hexagon generator for hexagons of the specified size."""
    def __init__(self, edge_length):
        self.edge_length = edge_length

    @property
    def col_width(self):
        return self.edge_length * 3

    @property
    def row_height(self):
        return np.sin(np.pi / 3) * self.edge_length

    def __call__(self, row, col):
        x = (col + 0.5 * (row % 2)) * self.col_width
        y = row * self.row_height
        for angle in range(0, 360, 60):
            x += np.cos(np.radians(angle)) * self.edge_length
            y += np.sin(np.radians(angle)) * self.edge_length
            yield x
            yield y
