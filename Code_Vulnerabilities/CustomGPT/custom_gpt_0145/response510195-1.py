
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

for angle_pair in angles:  # Loop over each pair of angles
    for x in angle_pair:  # For each angle in the pair
        for value in r:  # Loop over each value in r
            meq = (value * math.cos(math.radians(x)), value * math.sin(math.radians(x)))  # Calculate the new coordinates
            xylist.append(meq)  # Append the result to xylist

print(xylist)  # Output the resulting list
