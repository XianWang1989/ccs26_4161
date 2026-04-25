
import math
import numpy as np

# Define the radius values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# Define the angle pairs
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles list to a numpy array (not necessary in this case, but keeps it similar to your original)
angles = np.asarray(angles)

# Initialize an empty list to store results
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for x in angle_pair:
        for radius in r:
            # Calculate the x and y components
            x_component = radius * math.cos(math.radians(x))
            y_component = radius * math.sin(math.radians(x))
            # Append the result as a tuple
            xylist.append((x_component, y_component))

# Print the result
print(xylist)
