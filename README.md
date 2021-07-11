# Python Generative Art

This repository contains my Python setup for Generative Art

## Folder Structure

- pygenart: folder with basic tools, canvas, turtle...
- main.py: file used to draw, just create a function draw in draw section

# Examples
Reflected Gaussian Gradient
![Alt text](final\398_RGG3.png "Reflected Gaussian Gradient")

# Usage

python pixelpatterns.py 

### Args
Specify the color map to use, available are RGG, RGG2, RGG3

    -c RGG3

Specify the seeds list, to generate only 1 image just put 1 seed

    -s 909 125 398 
    -s 12

Specify the path to save the images

    -p final 
    
Specify the size, since images needs to be squared width and height are equal

    -N 2048

Generate a specified number of images with random seeds, in the example will generate 30 images, if -g is specified then -s become irrelevant

    -g 30

Some usage examples:

The following will create 3 images in the folder 'final' with seeds 909, 125, 398 using RGG3 as colormap, with a size of (2048, 2048)

    python pixelpatterns.py -c RGG3 -s 909 125 398 -p final -N 2048

This will generate 100 images in folder 'example_RGG3' with size (128, 128) and random seeds

    python pixelpatterns.py -c RGG3 -g 100 -p examples_RGG3 -N 128