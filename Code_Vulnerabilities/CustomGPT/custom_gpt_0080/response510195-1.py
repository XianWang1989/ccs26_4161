
import math
import numpy as np

# List of radius values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# List of angle tuples
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array
angles = np.asarray(angles)
xylist = []

# Iterate over each radius and corresponding angles
for i in range(len(angles)):
    for x in angles[i]:
        # Multiply each radius by cosine and sine of the angle
        meq = [r[i] * math.cos(math.radians(x)), r[i] * math.sin(math.radians(x))]
        xylist.append(meq)

print(xylist)
