
import math
import numpy as np

# Define the lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array for easier manipulation
angles = np.asarray(angles)

xylist = []
# Iterate through each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Iterate through r values
        for radius in r:
            # Calculate the x and y coordinates using cosine and sine
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # Append the result as a tuple to xylist
            xylist.append((x, y))

print(xylist)
