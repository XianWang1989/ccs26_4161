
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), 
          (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

angles = np.asarray(angles)
xylist = []

for angle_pair in angles:
    for r_value in r:
        x = angle_pair[0]
        y = angle_pair[1]

        # Calculate the x and y using r_value, angle x and y
        meq = [r_value * math.cos(math.radians(x)), 
                r_value * math.sin(math.radians(y))]
        xylist.append(meq)

print(xylist)
