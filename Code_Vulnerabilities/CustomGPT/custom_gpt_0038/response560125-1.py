
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length=50):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate offsets for the two diagonal lines
    offsets = np.arange(-length, length + 1)

    # Calculate the coordinates
    x1 = x_center + offsets * np.cos(angle_rad)
    y1 = y_center + offsets * np.sin(angle_rad)

    x2 = x_center + offsets * np.cos(angle_rad + np.pi / 2)
    y2 = y_center + offsets * np.sin(angle_rad + np.pi / 2)

    # Ensure coordinates are within the array boundaries
    x1, y1 = x1.astype(int), y1.astype(int)
    x2, y2 = x2.astype(int), y2.astype(int)

    # Extract the values from the array
    profile1 = array[y1, x1]
    profile2 = array[y2, x2]

    return profile1, profile2

# Extract the cross profile
center = (50, 50)
angle = 25
profile1, profile2 = extract_cross_profile(array, center, angle)

# Plot the original array and the cross profiles
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')

plt.subplot(1, 3, 2)
plt.plot(profile1, label='Diagonal 1 (25°)', color='blue')
plt.title('Profile at 25°')

plt.subplot(1, 3, 3)
plt.plot(profile2, label='Diagonal 2 (25° + 90°)', color='red')
plt.title('Profile at 115°')

plt.tight_layout()
plt.show()
