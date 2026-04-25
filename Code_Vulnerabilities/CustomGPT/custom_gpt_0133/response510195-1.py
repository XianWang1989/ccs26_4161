
import math
import numpy as np

# Input lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array
angles = np.asarray(angles)

# Initialize xylist
xylist = []

# Iterate over each angle pair from angles
for angle_pair in angles:
    # For each angle in the pair
    for angle in angle_pair:
        # Compute the results using list comprehension over the list `r`
        meq = [(value * math.cos(math.radians(angle)), value * math.sin(math.radians(angle))) for value in r]
        xylist.extend(meq)  # Use extend to flatten the list

# Print the resulting xylist
print(xylist)
