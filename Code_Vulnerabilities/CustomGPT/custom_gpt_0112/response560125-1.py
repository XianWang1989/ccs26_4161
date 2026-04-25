
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    # Get the size of the array
    rows, cols = arr.shape

    # Create the rotation matrix for the angle
    theta = np.radians(angle)
    cos_angle = np.cos(theta)
    sin_angle = np.sin(theta)

    # Generate cross profile coordinates
    cross_coords = []
    for d in range(-length, length + 1):
        x1 = int(center[0] + d * cos_angle)
        y1 = int(center[1] + d * sin_angle)
        x2 = int(center[0] + d * sin_angle)
        y2 = int(center[1] - d * cos_angle)

        # Check bounds and append if valid
        if 0 <= x1 < rows and 0 <= y1 < cols:
            cross_coords.append(arr[x1, y1])
        if 0 <= x2 < rows and 0 <= y2 < cols:
            cross_coords.append(arr[x2, y2])

    return np.array(cross_coords)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile
center = (50, 50)
angle = 25
length = 20  # Length of the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()

plt.figure()
plt.plot(cross_profile)
plt.title('Cross Profile at Angle 25°')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
