
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D Numpy array
array = np.random.rand(100, 100)

# Center point
center = (50, 50)
angle = 25  # in degrees

# Convert angle to radians
theta = np.radians(angle)

# Calculate the offset in the x and y directions
r = 20  # length of the profile along the line
x_offsets = np.linspace(-r, r, 2 * r + 1)
y_offsets1 = (x_offsets * np.tan(theta)).astype(int)  # slope for 25 degrees
y_offsets2 = -y_offsets1  # opposite slope for -25 degrees

# Extract the coordinates for the profile
coordinates1 = [(center[0] + x, center[1] + y) for x, y in zip(x_offsets, y_offsets1)]
coordinates2 = [(center[0] + x, center[1] + y) for x, y in zip(x_offsets, y_offsets2)]

# Get the values from the original array based on these coordinates
profile1 = [array[x, y] for x, y in coordinates1 if 0 <= x < 100 and 0 <= y < 100]
profile2 = [array[x, y] for x, y in coordinates2 if 0 <= x < 100 and 0 <= y < 100]

# Plotting just to visualize the array and the cross profile
plt.imshow(array, cmap='gray')
plt.plot(*zip(*coordinates1), color='red', label='25 degrees')
plt.plot(*zip(*coordinates2), color='blue', label='-25 degrees')
plt.legend()
plt.title('Diagonal Cross Profile at 25 Degrees')
plt.show()

print("Profile values at 25 degrees:", profile1)
print("Profile values at -25 degrees:", profile2)
