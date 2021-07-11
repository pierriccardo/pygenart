from PIL import Image
import numpy as np
from abc import abstractmethod
from pygenart.utils import distance

class Grid():
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
    
    @abstractmethod
    def apply(self):
        pass 

    def noise_gaussian(self, r, g, b):
        r += np.random.normal(1)*self.noise_value
        g += np.random.normal(1)*self.noise_value
        b += np.random.normal(1)*self.noise_value
        return r, g, b
    
    def noise_cellular(self, r, g, b, x, y):
        points = [(int(np.random.random() * self.unit), 
                    int(np.random.random() * self.unit)) 
                    for _ in range(self.noise_value)]

        min_dist_arr = []
        for p in points:
            min_dist_arr.append(distance(p[0], p[1], x, y))
    
        dist = np.min(min_dist_arr) 
        
        return r+dist*5, g+dist*5, b+dist*5

    def save(self, path):
        self.img.save(path)



class PixelGrid():

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
                            r, g, b, = self.noise_gaussian(r, g, b)


                        self.pixels[x, y] = int(r), int(g), int(b)
    

    def noise_gaussian(self, r, g, b):
        r += np.random.normal(1)*self.noise_value
        g += np.random.normal(1)*self.noise_value
        b += np.random.normal(1)*self.noise_value
        return r, g, b

    def save(self, path):
        self.img.save(path)

class HexagonalGrid(Grid):

    def __init__(self, size, unit, dpi=100, noise='gaussian', noise_value='10'):
        super().__init__(size, unit, dpi=dpi, noise=noise, noise_value=noise_value)

    def apply(self, cmap):
        
        for row in range(self.rows):
            for col in range(self.cols):

                # (row, col) is the center of the hexagon
                unit_row, unit_col = row*self.unit, col*self.unit
                cx = unit_row
                cy = unit_col
                size = self.unit
                w = int(size * np.sqrt(3))
                h = size * 2
                for x in range(max(0, cx-int(w/2)), min(cx+int(w/2), self.size[0])):
                    for y in range(int(0.5 - np.abs(x)/size)):

                        print(x)
                        print(y)
                        r, g, b = cmap[row, col]


                        self.pixels[x, y] = int(r), int(g), int(b)
                
                
                '''

                for x in range(unit_row, unit_row+self.unit):
                    for y in range(unit_col, unit_col+self.unit):

                        r, g, b = cmap[row, col]

                        if self.noise == 'gaussian':
                            r, g, b, = self.noise_gaussian(r, g, b)


                        self.pixels[x, y] = int(r), int(g), int(b)
                '''

        return super().apply()
    
