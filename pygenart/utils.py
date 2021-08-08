import numpy as np

def distance(x1, y1, x2, y2):
        return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def rgb2hex(rgb):
        r, g, b = rgb
        return '#%02x%02x%02x' % rgb

def rgb2int(rgb_tuple):
        return rgb_tuple[0] << 16 | rgb_tuple[1] << 8 | rgb_tuple[2]
        