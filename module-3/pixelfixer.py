#------------------------------------------------------------------------------
# pixelfixer.py: a command-line utility that fixes red-corrupted pixels in an
# RGB image.
#
# Run with:
#   python pixelfixer.py easy_corrupt_io_small.png
# which writes fixed_easy_corrupt_io_small.png next to the input.
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave


def compare_to_clean(Iq, bad, clean_file='clean_io_small.png'):
    """Print the largest color difference from the clean image at the bad pixels.

    Skips the comparison if the shapes differ or there are no bad pixels.
    """
    clean = imread(clean_file)
    if Iq.shape != clean.shape:
        print(f"Skipping clean check: {Iq.shape} vs {clean.shape}")
    elif not np.any(bad):
        print("Skipping clean check: no bad pixels")
    else:
        max_diff = np.max(np.abs(Iq[bad, :3] - clean[bad, :3]))
        print(f"Largest difference from clean at bad pixels: {max_diff}")


def pixelfix(I):
    """Replace bad pixels with the color averaged from their neighbors.

    Parameters
    ----------
    I : ndarray, shape (M, N, 3)
        A color image array in RGB format, values between 0 and 1.
        A bad pixel has red = 1, green = 0, blue = 0.

    Returns
    -------
    Iq : ndarray, same shape as I
        A copy of the image with the bad pixels fixed.
    """
    Iq = I.copy()

    ### YOUR WORK GOES HERE (with the agent, under the Protocol, in stages:
    ### 1. find the bad pixels and print how many;
    ### 2. paint them white and look at the result;
    ### 3. replace the white with the average of the up/down/left/right
    ###    neighbors. Then try solo_corrupt_io_small.png.)
    print(f"I.shape = {I.shape}")
    print(f"I.dtype = {I.dtype}")

    # True where a pixel is pure red, False everywhere else
    bad = (I[:,:,0] == 1) & (I[:,:,1] == 0) & (I[:,:,2] == 0)
    print(f"Number of bad pixels: {np.sum(bad)}")

    rows, cols = np.nonzero(bad)                    #positions of bad pixels

    up    = I[rows - 1, cols, :3]                   #neighbors' colors from I
    down  = I[rows + 1, cols, :3]
    left  = I[rows, cols - 1, :3]
    right = I[rows, cols + 1, :3]

    Iq[rows, cols, :3] = (up + down + left + right) / 4   #average, store in Iq

    # A pixel counts as changed if any of its channels differ
    changed = np.any(I != Iq, axis=2)
    print(f"Number of changed pixels: {np.sum(changed)}")

    compare_to_clean(Iq, bad)

    return Iq


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()

#I = np.zeros((100,200,3))
#print(I.shape)    
#print(I[:,:,0].shape)
#print(I[10,20])
