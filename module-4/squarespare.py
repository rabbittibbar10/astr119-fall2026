# Visualize equimaterial zones on a rolled cylinder

import numpy as np
import matplotlib.pyplot as plt

def product_remaining(r, R_new=3):
    """Fraction of product remaining by visible roll radius.

    Parameters
    ----------
    r : float, 1 <= r
        Visible radius of roll in units of r0, the cardboard cylinder radius.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0.

    Returns
    -------
    Current remaining length as fraction of original length of new roll.
    """
    return (r**2 - 1) /(R_new**2 -1) #my fraction

def product_visible(el_frac, R_new=3):
    """Visible roll radius by fraction of remaining product.

    Parameters
    ----------
    el_frac : float, 0 <= el_frac <= 1
        Current remaining length as fraction of original length of new roll.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.

    Returns
    -------
    Current visible radius of roll, in units of r0, the cardboard cylinder
    radius.
    """
    return np.sqrt(1 + el_frac*(R_new**2-1))

def visualize_danger(n, R_new=3, saveas=''):
    """Use n line segments of equal product to visualize paradox of the roll.

    Parameters
    ----------
    n : int scalar
        Number of line segments to display.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.
    saveas : str, optional, default: empty
        If not empty save figure to file 

    Returns
    -------
    None
    """

    # Start with a new figure window
    plt.close('all') # this helps get rid of old figures you forgot to close
    fh = plt.figure(figsize=(8,6)) # my favorite figure size

    ax = fh.add_subplot(1, 1, 1)
    ax.set_facecolor('white')

    # Core: grey disc of radius 1 with a black outline
    ax.add_patch(plt.Circle((0, 0), 1, facecolor='0.8', edgecolor='black',
                            linewidth=1.5))

    # Ring boundaries: each ring holds 1/n of the paper, not 1/n of the width
    for k in range(1, n + 1):
        r_k = product_visible(k / n, R_new)
        ax.add_patch(plt.Circle((0, 0), r_k, fill=False, edgecolor='black',
                                linewidth=1.5))

    # Axes: round circles, whole roll visible, frame but no ticks or grid
    margin = 0.1 * R_new
    ax.set_xlim(-R_new - margin, R_new + margin)
    ax.set_ylim(-R_new - margin, R_new + margin)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)

    # Title: n as a word, core fraction from R_new
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
             'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
             'nineteen', 'twenty']
    n_word = words[n] if 0 <= n < len(words) else str(n)
    core_frac = 'one third' if R_new == 3 else f'1/{R_new:g}'
    ax.set_title(f'{n_word} equal amounts of paper '
                 f'(core at {core_frac} of the radius)', fontsize=14)

    # Finally, show on screen and/or save to file
    if saveas:
        plt.savefig(saveas)
    plt.close()   # figures in this course are files: look at the saved PNG (plt.show() would pop a window instead)

if __name__ == '__main__':
    visualize_danger(5, saveas='roll_paradox_5.png')
    visualize_danger(3, saveas='roll_paradox_3.png')
    visualize_danger(9, saveas='roll_paradox_9.png')