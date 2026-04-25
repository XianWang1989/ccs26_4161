
import math
import numpy as np

# Define the values of r and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array (though not strictly necessary for this code)
angles = np.asarray(angles)
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Using list comprehension to multiply each r value by cos and sin of the angle
        meq = [(r_value * math.cos(math.radians(angle)), r_value * math.sin(math.radians(angle))) for r_value in r]
        xylist.append(meq)

# Print the result
print(xylist)
