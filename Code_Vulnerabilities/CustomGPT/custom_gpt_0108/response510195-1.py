
import math
import numpy as np

# Define the lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Initialize xylist
xylist = []

# Loop through angles and r
for angle_pair in angles:
    for r_value in r:
        meq = (r_value * math.cos(math.radians(angle_pair[0])), r_value * math.sin(math.radians(angle_pair[1])))
        xylist.append(meq)

# Print the result
print(xylist)
