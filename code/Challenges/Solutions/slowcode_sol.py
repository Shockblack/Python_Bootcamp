#--------------------------------
# Filename: slowcode_sol.py
#
# Description:
#   Solution to slowcode.py.
#   There could be numerous solutions.
#
# Author:
#   Aiden Zelakiewicz (asz39@cornell.edu)
#--------------------------------

import time
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u

start_time = time.time()

num_stars = 10000
ra = np.random.uniform(-1, 1, num_stars) * 360*u.deg
dec = np.random.uniform(-1, 1, num_stars) * 90*u.deg

sky = SkyCoord(ra, dec, frame='icrs')

l = sky.galactic.l
b = sky.galactic.b

gal_coord = np.array([l, b]).T

stop_time = time.time()
dt = stop_time-start_time


print(f"Took {dt} seconds")