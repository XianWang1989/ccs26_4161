
import math
import numpy as np

# List of radii
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]

# List of angle pairs
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Initialize an empty list for results
xylist = []

# Iterate over each angle in angles
for angle_pair in angles:
    for angle in angle_pair:
        # Create a temporary list to hold results for this angle
        results = []
        for radius in r:
            # Calculate x and y using cosine and sine for this radius and angle
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            results.append((x, y))  # Append the tuple (x, y) to results

        xylist.extend(results)  # Extend xylist with the current results
    print("Current angle pair:", angle_pair, "Results:", results)

print(xylist)
