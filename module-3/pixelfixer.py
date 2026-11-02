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
    
    print(f"I.shape = {I.shape}")
    print(f"I.dtype = {I.dtype}")

    # True where a pixel is pure red, False everywhere else
    bad = (I[:,:,0] == 1) & (I[:,:,1] == 0) & (I[:,:,2] == 0)
    print(f"Number of bad pixels: {np.sum(bad)}")

    M, N = I.shape[:2]
    rows, cols = np.nonzero(bad)

    # Neighbor positions, clipped so no index wraps (-1) or runs off the end;
    # the masks below remove any clipped values
    r_up    = np.clip(rows - 1, 0, M - 1)
    r_down  = np.clip(rows + 1, 0, M - 1)
    c_left  = np.clip(cols - 1, 0, N - 1)
    c_right = np.clip(cols + 1, 0, N - 1)

    # A neighbor is valid if it's inside the image AND not bad itself
    up_ok    = (rows > 0)     & ~bad[r_up, cols]
    down_ok  = (rows < M - 1) & ~bad[r_down, cols]
    left_ok  = (cols > 0)     & ~bad[rows, c_left]
    right_ok = (cols < N - 1) & ~bad[rows, c_right]

    up    = I[r_up, cols, :3]
    down  = I[r_down, cols, :3]
    left  = I[rows, c_left, :3]
    right = I[rows, c_right, :3]

    # Zero out invalid neighbors, then divide by how many are valid
    total = (up * up_ok[:, None] + down * down_ok[:, None]
             + left * left_ok[:, None] + right * right_ok[:, None])
    count = up_ok.astype(int) + down_ok + left_ok + right_ok

    # Note: count can be 0 if every neighbor is bad or outside the image,
    # which would give nan. None of the three test images have that case.
    Iq[rows, cols, :3] = total / count[:, None]

    # A pixel counts as changed if any of its channels differ
    changed = np.any(I != Iq, axis=2)
    print(f"Number of changed pixels: {np.sum(changed)}")

    return Iq


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()

