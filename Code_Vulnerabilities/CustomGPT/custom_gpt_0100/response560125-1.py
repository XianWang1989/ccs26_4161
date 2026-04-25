
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate the changes in x and y based on the angle
    dx = np.round(length * np.cos(theta)).astype(int)
    dy = np.round(length * np.sin(theta)).astype(int)

    # Create the line coordinates
    x = np.arange(center[0] - dx, center[0] + dx + 1)
    y = np.arange(center[1] - dy, center[1] + dy + 1)

    # Extract values along the diagonal lines
    cross_profile = []
    for i in range(len(x)):
        if 0 <= x[i] < array.shape[0] and 0 <= y[i] < array.shape[1]:
            cross_profile.append(array[x[i], y[i]])

    return np.array(cross_profile)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Specify the center and angle
center = (50, 50)
angle = 25  # degrees
length = 50  # half-length of the cross profile

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Display the results
print("Cross Profile Values:", cross_profile)

# Optional: visualize the array and the cross profile
plt.imshow(array, cmap='viridis')
plt.colorbar()
plt.title("Original 2D Array")
plt.scatter([center[0]], [center[1]], color='red')  # center point
plt.show()
