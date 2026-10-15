"""Equilibrium temperature of a planet orbiting a star (Pod 3)."""

import sys

import numpy as np
SIGMA = 5.67e-8  # Stefan-Boltzmann constant, W m^-2 K^-4


def t_eq(L, d):
    """Return the equilibrium temperature of a planet, in kelvin.

    L : luminosity of the star, in watts
    d : distance from the star to the planet, in meters

    Uses T_eq = (L / (16 pi sigma d^2))**(1/4).
    Check: the Sun (L = 3.8e26 W) at 1 AU (d = 1.496e11 m) gives about 278 K.
    """
    T_eq = (L / (16*np.pi*SIGMA*d**2))**(1/4)
    return T_eq



if __name__ == '__main__':
    L = float(sys.argv[1])  # first value after the script name
    d = float(sys.argv[2])
    T = t_eq(L, d)
    print(f"{T:.1f} K")
