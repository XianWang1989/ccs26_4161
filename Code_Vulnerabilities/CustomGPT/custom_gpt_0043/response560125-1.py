
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Convert angle to radians
    angle_rad = np.deg2rad(angle)

    # Get center coordinates
    x_center, y_center = center

    # Calculate the direction vectors
    delta_x = length * np.cos(angle_rad)
    delta_y = length * np.sin(angle_rad)

    # Calculate the coordinates of the cross
    coords = []

    # Create the cross lines
    for i in range(-length//2, length//2 + 1):
        # Calculate coordinates for one diagonal direction
        x1 = x_center + int(i * delta_x)
        y1 = y_center + int(i * delta_y)
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            coords.append(array[y1, x1])

        # Calculate coordinates for the opposite diagonal direction
        x2 = x_center - int(i * delta_x)
        y2 = y_center - int(i * delta_y)
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            coords.append(array[y2, x2])

    return np.array(coords)

# Example usage
array = np.random.rand(100, 100)
center = (50, 50)
angle = 25  # degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the extracted cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Array')
plt.imshow(array, cmap='gray')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Extracted Cross Profile')
plt.plot(cross_profile)
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.grid()
plt.show()
