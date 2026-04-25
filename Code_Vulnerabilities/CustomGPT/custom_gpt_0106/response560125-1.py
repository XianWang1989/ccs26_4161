
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Create an empty list to store the profile
    profile = []

    # Calculate the angle in radians
    theta = np.radians(angle)

    # Calculate sine and cosine of the angle
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    # Iterate over the length of the profile
    for i in range(-length // 2, length // 2 + 1):
        # Calculate the coordinates of the points in the cross profile
        x = int(center[0] + i * cos_theta)
        y = int(center[1] + i * sin_theta)

        # Check if the coordinates are within the array bounds
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile.append(array[x, y])

    return np.array(profile)

# Create a 100x100 example array
array = np.random.rand(100, 100)

# Define center, angle, and length of the cross profile
center = (50, 50)
angle = 25  # degrees
length = 20  # length of the profile

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the cross profile
plt.imshow(array, cmap='gray', interpolation='none')
plt.scatter(center[1], center[0], color='red')  # center point
plt.title("Original Array")
plt.colorbar()
plt.show()

plt.plot(cross_profile)
plt.title("Cross Profile at 25 Degrees")
plt.xlabel("Profile Index")
plt.ylabel("Intensity")
plt.grid()
plt.show()
