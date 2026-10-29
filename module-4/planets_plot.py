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
    fig, (ax2,ax) = plt.subplots(1,2, figsize = (12,6)) 
    fig.suptitle("Planet temperature vs orbital distance from host star")
    ax2.set_title("Linear axis")
    #plot each planet as a point, distance in AU and temp in K
    ax.scatter(dist, T, label = "Planets")
    ax.set_xlabel("Orbital distance from host star (AU)")
    ax.set_ylabel("Temperature (K)")
    ax.set_title("Log axis")
    #build curve, 0.01 to 2 AU
    d = np.linspace(0.01, 2.0, 200)
    T_curve = t_eq(L_SUN, d * AU)  #curve for a sunlike star
    T_half = t_eq(0.5*L_SUN, d*AU) #curve for a star with half luminosity of sun                                                     
    #change axis to log, curve will be a straight line
    ax.set_xscale("log") 
    ax.set_yscale("log")
    ax.plot(d, T_curve, label = r"Sun-like star (1L$_\odot$)")
    ax.plot(d, T_half, linestyle = "--", label = r"Half Sun-like star (0.5L$_\odot$)")
    ax2.scatter(dist, T, label="Planets") #linear axes
    ax2.set_xlabel("Orbital distance from host star (AU)")
    ax2.set_ylabel("Temperature (K)")
    ax2.plot(d, T_curve, label=r"Sun-like star (1L$_\odot$)")
    ax2.plot(d, T_half, linestyle="--", label=r"Half Sun-like star (0.5L$_\odot$)")

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
    for n, x, y in zip(name, dist, T):
        dx, dy = offsets.get(n, (5, 5))   # everyone else: up and right
        ax2.annotate(n, (x, y), xytext=(dx, dy), textcoords="offset points", fontsize=8)
    ax.legend()
    ax2.legend()
    fig.savefig("module-4/planets.png", dpi=130)
    print("wrote module-4/planets.png")
    loss_per_orbit = 5.586 #radius lost per orbit in m
    R = np.linspace(100,5000,200) #comet radius, 100m to 5km, 200 values evenly spaced
    orbits_left = R/loss_per_orbit #orbits until comet is burnt out
    fig2, ax2 = plt.subplots(figsize = (8,6))
    ax2.plot(R, orbits_left, label="5.586m lost per orbit") #linear axis so proportional relation is straight line
    ax2.set_xlabel("Comet radius (m)")
    ax2.set_ylabel("Orbits remaining")
    ax2.set_title("Comet lifetime vs. radius ")
    ax2.legend()
    fig2.savefig("module-4/comet_lifetime.png", dpi=150)
    print("wrote module-4/comet_lifetime.png")


    
I = plt.imread("module-3/clean_io_small.png") #read in io image from module 4
print(I.shape, I.dtype, I.min(), I.max()) #check the size and value range of the image
fig, (ax,ax2) = plt.subplots(1,2,figsize=(12,5))
ax.hist(I[:,:,0].ravel(), bins=50) #[:,:,0] is the red chanel and .ravel() flattens 2D to 1D
ax2.hist(I[:,:,0][I[:,:,0]>0.02], bins=50) #only keep the red vals above 0.02, removing the black background
ax.set_xlabel("Red value")
ax.set_ylabel("Number of pixels")
ax.set_title("Histogram of red values in the Io image")
ax2.set_title("Histogram with background removed")
fig.savefig("module-4/io_red_hist.png", dpi=150)
print("wrote module-4/io_red_hist.png")
#the big spike is on the far left of the histogram, at 0, and comes from the background