# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0

if __name__ == "__main__":
    print("shape:", I.shape)
print(I.size)
print(I[0,0])
print(I[356,349])

J = I.copy()
J[20:40, 20:40, :] = 1 # add white dot
J[356, :, :] = 0 # add black line
imsave("module-3/pixels_out.png", J)
neg = I.copy()
neg = 1-neg
imsave("module-3/pixels_neg.png", neg)
falsec = I.copy()
falsec[:,:,2] = 1 - falsec[:,:,0]
h, w = falsec.shape[:2]
falsec[h//4 : h//4 + 20, w//2 - 60 : w//2 - 40, :] = 0   # left eye
falsec[h//4 : h//4 + 20, w//2 + 40 : w//2 + 60, :] = 0   # right eye
falsec[h//4 + 60 : h//4 + 75, w//2 - 60 : w//2 + 60, :] = [1, 0, 0]   # red mouth
imsave("module-3/pixels_falsec.png", falsec)