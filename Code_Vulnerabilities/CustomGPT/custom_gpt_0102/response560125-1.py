
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
arr = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(arr, center, angle, length=50):
    y, x = center
    angle_rad = np.radians(angle)

    # Calculate coordinates for the cross profile
    delta_x = np.cos(angle_rad) * length
    delta_y = np.sin(angle_rad) * length

    # Create a list of coordinates for the profile
    coords = [(int(y + delta_y * i), int(x + delta_x * i)) for i in range(-length, length + 1)]

    # Extract values while avoiding out-of-bounds indices
    profile_values = [arr[i, j] for (i, j) in coords if 0 <= i < arr.shape[0] and 0 <= j < arr.shape[1]]

    return np.array(profile_values)

# Extract the cross profile
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(arr, center, angle)

# Display the results
plt.plot(cross_profile)
plt.title(f'Cross Profile at {angle} degrees')
plt.xlabel('Profile Distance')
plt.ylabel('Value')
plt.show()
