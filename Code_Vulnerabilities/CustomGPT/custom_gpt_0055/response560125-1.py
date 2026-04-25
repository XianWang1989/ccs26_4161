
import numpy as np
import math

# Create a 100x100 array
array = np.random.rand(100, 100)

# Center coordinates
center = (50, 50)

# Angle in degrees
angle = 25
radians = math.radians(angle)

# Calculate slope and intercepts
slope = math.tan(radians)

# Length for cross profile
length = 30
cross_profile = []

# Extract points from the cross profile
for i in range(-length, length + 1):
    # Diagonal line coordinates
    x1 = center[0] + i
    y1 = center[1] + int(slope * i)
    x2 = center[0] + int(slope * i)
    y2 = center[1] + i

    # Ensure coordinates are within bounds
    if 0 <= x1 < 100 and 0 <= y1 < 100:
        cross_profile.append(array[y1, x1])
    if 0 <= x2 < 100 and 0 <= y2 < 100:
        cross_profile.append(array[y2, x2])

# Remove duplicates if any
cross_profile = list(set(cross_profile))

print("Cross profile values:", cross_profile)
