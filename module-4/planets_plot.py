# planets_plot_starter.py -- the ten planets as arrays, ready to plot (Pod 6). Copy this file to planets_plot.py and work on the copy.
# Run from the repository folder:  python module-4/planets_plot.py
import numpy as np
import matplotlib.pyplot as plt

SIGMA = 5.67e-8          # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26           # solar luminosity, W
AU = 1.496e11            # meters per AU

name = np.array(["Earth", "Mars", "HD 209458 b", "51 Peg b", "TRAPPIST-1 e",
                 "Kepler-22 b", "55 Cnc e", "HD 189733 b", "Kepler-452 b", "Proxima b"])
lum = np.array([1.0, 1.0, 1.6, 1.3, 0.00055, 0.79, 0.58, 0.34, 1.2, 0.0016])        # star luminosity, solar units
dist = np.array([1.000, 1.524, 0.047, 0.052, 0.029, 0.85, 0.0154, 0.031, 1.046, 0.0485])   # distance, AU


def t_eq(L, d):
    """Equilibrium temperature (K) at distance d (m) from a star of luminosity L (W)."""
    return (L / (16 * np.pi * SIGMA * d**2)) ** 0.25


if __name__ == "__main__":
    #equilibrium temp of each planet
    T = t_eq(lum * L_SUN, dist * AU)
    #create figure and set of axes
    fig, ax = plt.subplots(figsize = (8,6)) 
    #plot each planet as a point, distance in AU and temp in K
    ax.scatter(dist, T, label = "Planets")
    ax.set_xlabel("Distance (AU)")
    ax.set_ylabel("Temperature (K)")
    #build curve, 0.01 to 2 AU
    d = np.linspace(0.01, 2.0, 200)
    T_curve = t_eq(L_SUN, d * AU)
    #change axis to log, curve will be a straight line
    ax.set_xscale("log") 
    ax.set_yscale("log")
    ax.plot(d, T_curve, label = "Sun-like star (1L_sun)")
    #label each planet
    # custom (x, y) offsets in points for planets in crowded spots
    offsets = {
        "HD 209458 b":  (6, 6),
        "51 Peg b":     (6, -10),
        "HD 189733 b":  (-60, -4),
        "Kepler-22 b":  (-58, 4),
        "Earth":        (-10, -14),
        "Kepler-452 b": (6, 6),
        "TRAPPIST-1 e": (-30, -14),
    }
    for n, x, y in zip(name, dist, T):
        dx, dy = offsets.get(n, (5, 5))   # everyone else: up and right
        ax.annotate(n, (x, y), xytext=(dx, dy), textcoords="offset points", fontsize=8)
    ax.legend()
    fig.savefig("module-4/planets.png", dpi=150)
    print("wrote module-4/planets.png")
