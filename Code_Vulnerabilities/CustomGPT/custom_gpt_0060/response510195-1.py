
import math
import numpy as np

# Your lists of floats
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Initialize an empty list for the results
xylist = []

# Iterate over each angle in the angles array
for angle_pair in angles:
    for x in angle_pair:
        # You should iterate over the r values separately
        for r_value in r:
            # Calculate the cosine and sine based on the angle
            x_cos = r_value * math.cos(math.radians(x))
            x_sin = r_value * math.sin(math.radians(x))

            # Create a tuple for the x and y values and append it to the xylist
            xylist.append((x_cos, x_sin))

print(xylist)
