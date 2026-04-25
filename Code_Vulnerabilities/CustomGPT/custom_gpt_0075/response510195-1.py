
import math

# List of radius values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# List of angle tuples
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []

# Iterate through angle pairs and radius
for angle in angles:
    for r_value in r:
        # Calculate x and y using the formula
        x = r_value * math.cos(math.radians(angle[0]))
        y = r_value * math.sin(math.radians(angle[1]))
        xylist.append((x, y))

print(xylist)
