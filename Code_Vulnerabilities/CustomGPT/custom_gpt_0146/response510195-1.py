
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []

# Convert 'angles' to a numpy array if you won't need the functionality of a list
angles = np.asarray(angles)

# Iterate through each angle tuple
for angle_tuple in angles:
    for x in angle_tuple:
        # Create a temp list to hold results for each r
        for radius in r:
            meq = [radius * math.cos(math.radians(x)), radius * math.sin(math.radians(x))]
            xylist.append(meq)

print(xylist)
