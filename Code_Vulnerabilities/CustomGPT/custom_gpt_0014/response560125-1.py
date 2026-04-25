
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(array, center, angle, width=5):
    y, x = center
    angle_rad = np.deg2rad(angle)

    delta_x = np.array([np.cos(angle_rad), np.sin(angle_rad)]) * width
    delta_y = np.array([-np.sin(angle_rad), np.cos(angle_rad)]) * width

    profile = []

    for i in range(-width, width + 1):
        x1 = int(x + i * delta_x[0])
        y1 = int(y + i * delta_x[1])

        x2 = int(x + i * delta_y[0])
        y2 = int(y + i * delta_y[1])

        if 0 <= x1 < array.shape[1] and 0 <= y1 < array.shape[0]:
            profile.append(array[y1, x1])
        if 0 <= x2 < array.shape[1] and 0 <= y2 < array.shape[0]:
            profile.append(array[y2, x2])

    return np.array(profile)

# Define center and angle
center = (50, 50)
angle = 25

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle)

# Print the cross profile
print(cross_profile)

# Optional: Visualization
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.scatter([center[1]], [center[0]], color='red')
plt.show()
