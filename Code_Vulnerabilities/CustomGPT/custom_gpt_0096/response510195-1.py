
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), 
          (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []
for angle_pair in angles:
    for x in angle_pair:
        for radius in r:
            meq = (radius * math.cos(math.radians(x)), radius * math.sin(math.radians(x)))
            xylist.append(meq)

print(xylist)
