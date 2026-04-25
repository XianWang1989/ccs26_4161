
import math
import numpy as np

# Your radius list
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# Your angles as a numpy array
angles = np.asarray([(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)])

xylist = []
# Iterate over both the radius list and the angles
for angle in angles:
    for radius in r:
        # Calculate the x and y using the current angle and radius
        x = radius * math.cos(math.radians(angle[0]))
        y = radius * math.sin(math.radians(angle[1]))
        xylist.append([x, y])

print(xylist)
