
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length=50):
    rows, cols = arr.shape
    x_center, y_center = center
    theta = np.radians(angle)

    # Calculate offset for the diagonal lines
    dx = length * np.cos(theta) 
    dy = length * np.sin(theta)

    # Create lists to store the coordinates of the cross profile
    profile = []

    for d in range(-length, length + 1):
        # Calculate the coordinates for the left and right diagonal lines
        x_left = int(x_center + d * dy)
        y_left = int(y_center + d * dx)
        x_right = int(x_center - d * dy)
        y_right = int(y_center - d * dx)

        # Append to profile if within bounds
        if 0 <= x_left < rows and 0 <= y_left < cols:
            profile.append(arr[x_left, y_left])
        if 0 <= x_right < rows and 0 <= y_right < cols:
            profile.append(arr[x_right, y_right])

    return np.array(profile)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Print the result
print(cross_profile)

# Optionally, visualize the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter([center[1]], [center[0]], color='red')  # Center point
plt.title('Original Array with Center Point')
plt.show()
