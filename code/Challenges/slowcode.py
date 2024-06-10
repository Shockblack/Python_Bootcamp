#--------------------------------
# Filename: slowcode.py
#
# Description:
#   Exercise in optimizing slow code.
#   Goal is to convert a simulated list of 
#   RA and Dec into l and b coordinates.
#
# Author:
#   Aiden Zelakiewicz (asz39@cornell.edu)
#--------------------------------

import time
import scipy
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u

start_time = time.time()

num_stars = 10000

gal_coord = []

for i in range(num_stars):
    ra = np.random.uniform(-1, 1, 1) * 360*u.deg
    dec = np.random.uniform(-1, 1, 1) * 90*u.deg
    sky = SkyCoord(ra, dec, frame='icrs')

    l = sky.galactic.l
    b = sky.galactic.b

    gal_coord.append((l,b))

stop_time = time.time()
dt = stop_time-start_time


print(f"Took {dt} seconds")