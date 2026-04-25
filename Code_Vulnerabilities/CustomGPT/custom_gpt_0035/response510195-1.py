
import math

# Define the radius list and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []

# Iterate over the angles
for angle_pair in angles:
    for angle in angle_pair:
        for radius in r:
            meq = [radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle))]
            xylist.append(meq)

print(xylist)
