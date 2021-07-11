from numpy.random import seed
from tqdm import tqdm

import numpy as np
import argparse
import os

#------------------------------
# ARGS PARSER
#------------------------------
parser = argparse.ArgumentParser(description='Parameters shortcut for generative art')
parser.add_argument('--size',       '-N',   type=int,  default=256,     help='specify dimension (img needs to be squared)')
parser.add_argument('--generate',   '-g',   type=int,  default=1,       help='specify format of the image')
parser.add_argument('--cmap',       '-c',   type=str,  default='RGG',   help='specify the color map to use', required=True)
parser.add_argument('--path',       '-p',   type=str,  default='img',   help='specify the path to save the image')
parser.add_argument('--seeds',      '-s',   type=int,  default=[0],     help='list of seeds to generate', nargs='+')
parser.add_argument('--noise',      '-n',   type=str,  default='none',  help='choose the noise for the image')
parser.add_argument('--noise_value','-nv',  type=int,  help='choose the noise value for the image')
args = parser.parse_args()

#------------------------------
# PARAMS
#------------------------------

N = args.size
unit = int(N/16)
size = (N, N)
w, h = size
rows = int(w / unit)
cols = int(h / unit)
PATH = f'img/pixelpatterns/{args.path}'
if not os.path.exists(PATH):
  os.makedirs(PATH)
  

print()

# ------------------------------
# Experiment
# ------------------------------
from pygenart.grids import PixelGrid, HexagonalGrid
from pygenart.cmaps import Cmap

def exp(seed):
    np.random.seed(seed=seed)

    cmaps = Cmap(rows, cols)
    cmap = cmaps.getmap(args.cmap)    
    noise_value = int(0.023 * N + 4.29) if args.noise_value is None else args.noise_value

    #img = PixelGrid(size, unit, noise=args.noise, noise_value=noise_value)
    img = HexagonalGrid(size, unit, noise=args.noise, noise_value=noise_value)
    img.apply(cmap)

    img.save(f'{PATH}/{seed}_{args.cmap}.png')
    img.save(f'img/latest.png')

# seeds 
if args.generate > 1:
    seeds = [int(np.random.random() * 1000) for _ in range(args.generate)]
else:
    seeds = args.seeds

pbar = tqdm(seeds)
for s in pbar:
  pbar.set_description(f'[current seed: {s}]')
  exp(s)
