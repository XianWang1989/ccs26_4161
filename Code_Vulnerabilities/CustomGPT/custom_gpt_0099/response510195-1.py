
import math
import numpy as np

# Define the lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a NumPy array for easier manipulations
angles = np.asarray(angles)

# Create an empty list for results
xylist = []

# Loop through each angle tuple
for angle in angles:
    for x in angle:
        # Multiply each r value by the cosine and sine of the angle x
        meq = [(value * math.cos(math.radians(x)), value * math.sin(math.radians(x))) for value in r]
        xylist.extend(meq)  # Add results to xylist

# Print the result
print(xylist)
