
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate offsets based on the angle
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Generate the coordinates for the cross
    coords = []
    for offset in range(-length//2, length//2 + 1):
        x1 = int(x_center + offset * dx)
        y1 = int(y_center + offset * dy)
        x2 = int(x_center - offset * dx)
        y2 = int(y_center - offset * dy)

        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            coords.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            coords.append(array[x2, y2])

    return np.array(coords)

# Define center and angle
center = (50, 50)
angle = 25
length = 40

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the extracted profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.plot(cross_profile, marker='o')
plt.title('Extracted Cross Profile')
plt.xlabel('Sample Points')
plt.ylabel('Value')
plt.grid()

plt.show()
