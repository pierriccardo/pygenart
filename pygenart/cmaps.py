import numpy as np
from pygenart.utils import distance

class Cmap():

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols
    
    def getmap(self, cmap):
        if cmap == 'RGG':
            return self.RGG()
        elif cmap == 'RGG2':
            return self.RGG2()
        elif cmap == 'RGG3':
            return self.RGG3()
        elif cmap == 'RGG4':
            return self.RGG4()
        else:
            print(f'error: {cmap} color map not found')
    
    def reflection(self, x, y, colors, r, g, b):
        x_arr = [x, self.rows-x-1]
        y_arr = [y, self.cols-y-1]
        for j in x_arr:
            for k in y_arr:
                colors[k, j] = colors[j, k] = (r, g, b)

    def RGG(self): # Reflected Gaussian Gradient
        colors = np.ndarray(shape=(self.rows, self.cols, 3), dtype=int)
        c = 10

        center = (int(self.rows / 2), int(self.cols / 2))
        for x in range(self.rows):
            for y in range(self.cols):

                r = int(((x - center[0]) * 255) / self.rows + np.random.normal(1) * c)
                g = int(((y - center[1]) * 255) / self.cols + np.random.normal(1) * c)
                b = 200

                self.reflection(x, y, colors, r, g, b)
        return colors 

    def RGG2(self): # Reflected Gaussian Gradient
        colors = np.ndarray(shape=(self.rows, self.cols, 3))
        c = 10

        center = (int(self.rows / 2), int(self.cols / 2))
        for x in range(self.rows):
            for y in range(self.cols):

                g = int(((x - center[0]) * 255) / self.rows + np.random.normal(1) * c)
                r = int(((y - center[1]) * 255) / self.cols + np.random.normal(1) * c)
                b = 200

                self.reflection(x, y, colors, r, g, b)
        return colors

    def RGG3(self): # Reflected Gaussian Gradient
        colors = np.ndarray(shape=(self.rows, self.cols, 3))

        # center
        c_x = int(self.rows * np.random.random())
        c_y = int(self.cols * np.random.random())

        for x in range(self.rows):
            for y in range(self.cols):
                dist = distance(c_x, c_y, x, y)

                g = int(dist*x + dist*np.random.normal(1))
                r = int(dist*y + dist*np.random.normal(1))
                b = int(np.random.normal(1)*x + np.random.normal(1)*y)

                self.reflection(x, y, colors, r, g, b)
        return colors
    
    def RGG4(self): # Reflected Gaussian Gradient
        colors = np.ndarray(shape=(self.rows, self.cols, 3))

        # center
        c_x = int(self.rows * np.random.random())
        c_y = int(self.cols * np.random.random())

        for x in range(self.rows):
            for y in range(self.cols):
                dist = distance(c_x, c_y, x, y)

                r = dist*x + dist*np.random.normal(1)
                g = dist*y + dist*np.random.normal(1)
                b = np.random.normal(1)*x + np.random.normal(1)*y

                self.reflection(x, y, colors, r, g, b)
                
        return colors