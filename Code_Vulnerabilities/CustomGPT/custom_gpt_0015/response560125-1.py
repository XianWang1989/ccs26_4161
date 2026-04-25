
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

# Function to extract diagonal cross profile
def extract_cross_profile(array, center, angle, length):
    # Convert angle from degrees to radians
    theta = np.radians(angle)

    # Calculate direction vectors
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Define the coordinates for the cross profile
    coordinates = []
    for i in range(-length//2, length//2):
        x1 = center[0] + i * dx
        y1 = center[1] + i * dy
        x2 = center[0] - i * dx
        y2 = center[1] - i * dy

        # Clip coordinates to the array bounds
        x1, y1 = np.clip([x1, y1], 0, array.shape[0] - 1).astype(int)
        x2, y2 = np.clip([x2, y2], 0, array.shape[0] - 1).astype(int)

        coordinates.append((x1, y1))
        coordinates.append((x2, y2))

    # Extract values from the array
    profile_values = [array[x, y] for x, y in coordinates]
    return np.array(profile_values)

# Center point
center = (50, 50)
# Angle and length of the cross profile
angle = 25  # degrees
length = 50  # length of the profile

# Extract the diagonal cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Visualization of the original array and the profile
plt.imshow(array, cmap='gray')
plt.title('Original 2D Array')
plt.colorbar()
plt.show()

plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Position Along Profile')
plt.ylabel('Value')
plt.show()
