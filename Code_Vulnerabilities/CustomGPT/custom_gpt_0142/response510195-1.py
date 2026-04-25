
import math
import numpy as np

# Your radius list
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# Your angles as a list of tuples
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Converting angles into a NumPy array (which you were already doing)
angles = np.asarray(angles)
xylist = []

# Nested loop to compute x and y for each angle and r value
for angle in angles:
    for radius in r:
        # Calculate x and y using cosine and sine
        x = radius * math.cos(math.radians(angle[0]))
        y = radius * math.sin(math.radians(angle[1]))
        # Append the result as a tuple
        xylist.append((x, y))

# Print the results
print(xylist)
