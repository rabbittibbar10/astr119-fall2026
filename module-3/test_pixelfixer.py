#------------------------------------------------------------------------------
# test_pixelfixer.py: checks that the fixed images have no bad pixels left, and
# that the check really does detect bad pixels in an unfixed image.
#
# Run from inside module-3, after running pixelfixer.py on all three images:
#   python test_pixelfixer.py
#------------------------------------------------------------------------------
import numpy as np
from matplotlib.pyplot import imread


def assert_no_bad_pixels(image_file):
    """Raise an AssertionError if image_file has any pure red pixels."""
    I = imread(image_file)
    bad = (I[:,:,0] == 1) & (I[:,:,1] == 0) & (I[:,:,2] == 0)
    n_bad = np.sum(bad)
    assert n_bad == 0, f"{image_file} has {n_bad} bad pixels"


def _main():
    for name in ['easy', 'solo', 'full']:
        image_file = f'fixed_{name}_corrupt_io_small.png'
        assert_no_bad_pixels(image_file)
        print(f"PASS: {image_file}")

    # The unfixed image must fail, or the check above proves nothing
    try:
        assert_no_bad_pixels('full_corrupt_io_small.png')
    except AssertionError as error:
        print(f"PASS: detected as expected: {error}")
    else:
        raise AssertionError("The check missed the bad pixels in the unfixed image")


if __name__ == '__main__':
    _main()
