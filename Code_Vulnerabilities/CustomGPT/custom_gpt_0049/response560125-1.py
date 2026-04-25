
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    # Convert angle from degrees to radians
    angle_rad = np.radians(angle)

    # Calculate direction vectors based on the angle
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Generate coordinates for the cross profile
    cross_profile = []
    for i in range(-length, length + 1):
        x1 = int(center[0] + i * dx)
        y1 = int(center[1] + i * dy)
        if 0 <= x1 < arr.shape[0] and 0 <= y1 < arr.shape[1]:
            cross_profile.append(arr[x1, y1])

        # Perpendicular direction
        x2 = int(center[0] + i * -dy)
        y2 = int(center[1] + i * dx)
        if 0 <= x2 < arr.shape[0] and 0 <= y2 < arr.shape[1]:
            cross_profile.append(arr[x2, y2])

    return cross_profile

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center_point = (50, 50)           # Center at (50, 50)
angle = 25                         # Angle of 25 degrees
length = 25                        # Length of the cross profile

cross_profile = extract_cross_profile(array, center_point, angle, length)

# Plotting the original array and the cross profile for visualization
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.plot(cross_profile, marker='o')
plt.title('Diagonal Cross Profile')
plt.xlabel('Profile Points')
plt.ylabel('Values')
plt.grid()

plt.show()
