
import math

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Multiply each `r` value by the cosine and sine of the angle
        for value in r:
            meq = (value * math.cos(math.radians(angle)), value * math.sin(math.radians(angle)))
            xylist.append(meq)

print(xylist)
