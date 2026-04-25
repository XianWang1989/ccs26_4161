
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    y0, x0 = center
    angle_rad = np.radians(angle)

    # Create two lists to hold the coordinates of the cross profile
    coords = []

    # Calculate the offset based on the angle
    delta_x = np.cos(angle_rad)
    delta_y = np.sin(angle_rad)

    for d in range(-length//2, length//2 + 1):
        # Calculate new coordinates
        x = int(x0 + d * delta_x)
        y = int(y0 + d * delta_y)
        if 0 <= x < cols and 0 <= y < rows:
            coords.append(array[y, x])

    return np.array(coords)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)
angle = 25
length = 50

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the extracted cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Extracted Cross Profile')
plt.xlabel('Distance along cross profile')
plt.ylabel('Intensity')

plt.show()
