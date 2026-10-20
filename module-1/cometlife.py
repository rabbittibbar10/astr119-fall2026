#ask for comet's radius and estimates how much radius shrinks per orbit
#run from astr119/module-1 folder with python cometlife.py
from math import pi, sqrt
km = 1000 #m
AU = 1.49e11 #m
L_sol = 3.8e26 #J/s
GM_sol = 1.3271e20 #m^3/s^2
h_ice = 2.5e6 #J/kg
R_km = float(input("What is the radius (in km): "))
R_user = R_km*km
def comet(R =2*km, A = 0, p = 500, a = 3.12*(AU), e = 0.5 ):
    """Return (dr in  m, number of orbits) for a comet of radius R [m].""" #R in m, p in kg/m^3, a in m
    H_sol = (pi / 2) * (1 - A) * R**2 * (L_sol) / ( sqrt(GM_sol)*sqrt( a*(1-e**2) ) )  
    dM = H_sol / h_ice
    dr = dM / (4 * pi * R**2 * p)
    orbits = R / dr
    return dr, orbits


#baseline
dr0, orbits0 = comet(R=R_user) #user inputed radius is used
print(f"For R = {R_km}: dr = {dr0:.2f}m, the comet lasts {orbits0:.0f} orbits")

# albedo 0.5
dr_A, orbits_A = comet(R = R_user, A = 0.3) #change A
print(f"With albedo 0.5, dr = {dr_A:.2f}m, and the comet lasts {orbits_A:.0f} orbits,"
      f" {orbits_A/orbits0:.1f} times longer, because it absorbs only half the sunlight")

#radius of 1km # change R
dr_R, orbits_R = comet(R = 1*km)
print(f"R = 1km: dr = {dr_R:.2f}m (unchanged), but the comet only lasts {orbits_R:.0f} orbits,"
      f" {orbits_R/orbits0:.1f} times as many, because dr does not depend on R, so the comet has less radius to lose")


#HW1 pt 2
#lifetime in years: by keplers 3rd law, one orbit takes a**1.5 yrs
years = orbits0 * 3.12**1.5
print(f"With R = {R_km}km and albedo 0, the comet will last about {years:.0f} years")
