
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array for demonstration
array = np.random.rand(100, 100)

# Center point
center = (50, 50)

# Angle in degrees
angle = 25
theta = np.radians(angle)

# Calculate the direction of the diagonal
dx = np.cos(theta)
dy = np.sin(theta)

# Length of the cross profile (you can adjust this)
length = 50

# Extract indices along the diagonal cross
x_coords = []
y_coords = []

for i in range(-length, length + 1):
    x = int(center[0] + i * dx)
    y = int(center[1] + i * dy)
    if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
        x_coords.append(x)
        y_coords.append(y)

# Extract the values from the array
cross_profile = array[x_coords, y_coords]

# Display the original array and the cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.scatter(y_coords, x_coords, color='red')  # plot the cross profile on the original array
plt.title("Original Array with Cross Profile")
plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title("Diagonal Cross Profile")
plt.xlabel("Index along Cross Profile")
plt.ylabel("Value")
plt.show()
