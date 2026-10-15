"""Equilibrium temperature of a planet orbiting a star (Pod 3)."""

import sys

import numpy as np
SIGMA = 5.67e-8  # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26   # one solar luminosity, W
AU = 1.496e11    # one astronomical unit, m


def t_eq(L, d):
    """Return the equilibrium temperature of a planet, in kelvin.

    L : luminosity of the star, in watts
    d : distance from the star to the planet, in meters

    Uses T_eq = (L / (16 pi sigma d^2))**(1/4).
    Check: the Sun (L = 3.8e26 W) at 1 AU (d = 1.496e11 m) gives about 278 K.
    """
    T_eq = (L / (16*np.pi*SIGMA*d**2))**(1/4)
    return T_eq

planets = [   # name, luminosity (solar units), distance (AU)
    ["Earth",        1.0,     1.000],
    ["Mars",         1.0,     1.524],
    ["HD 209458 b",  1.6,     0.047],
    ["51 Peg b",     1.3,     0.052],
    ["TRAPPIST-1 e", 0.00055, 0.029],
    ["Kepler-22 b",  0.79,    0.85],
    ["55 Cnc e",     0.58,    0.0154],
    ["HD 189733 b",  0.34,    0.031],
    ["Kepler-452 b", 1.2,     1.046],
    ["Proxima b",    0.0016,  0.0485],
]


if __name__ == '__main__':
    L = float(sys.argv[1])  # first value after the script name
    d = float(sys.argv[2])
    T = t_eq(L, d)
    print(f"{T:.1f} K")

    for i in range(len(planets)):
        name = planets[i][0]
        L_i = planets[i][1] * L_SUN   # solar luminosities -> W
        d_i = planets[i][2] * AU      # AU -> m
        print(f"{name:<14}{t_eq(L_i, d_i):>6.0f} K")
