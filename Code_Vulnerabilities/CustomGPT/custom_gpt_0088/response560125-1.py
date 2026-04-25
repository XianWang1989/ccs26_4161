
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 sample array
array = np.random.rand(100, 100)

# Function to extract diagonal cross profile
def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Create arrays for the x and y offsets
    offsets = np.arange(-length, length + 1)

    # Calculate the x and y offsets based on the angle
    x_offsets = offsets * np.cos(angle_rad)
    y_offsets = offsets * np.sin(angle_rad)

    # Calculate the coordinates for the cross profile
    coords1 = np.array([x_center + x_offsets, y_center + y_offsets]).T
    coords2 = np.array([x_center - x_offsets, y_center + y_offsets]).T

    # Gather the values from the array
    profile1 = array[coords1[:, 1].astype(int), coords1[:, 0].astype(int)]
    profile2 = array[coords2[:, 1].astype(int), coords2[:, 0].astype(int)]

    return profile1, profile2

# Extract the cross profile
cross_profile1, cross_profile2 = extract_cross_profile(array, (50, 50), 25, 25)

# Plotting the profiles
plt.plot(cross_profile1, label='Diagonal 1')
plt.plot(cross_profile2, label='Diagonal 2')
plt.title('Diagonal Cross Profile at 25 degrees')
plt.xlabel('Offset')
plt.ylabel('Value')
plt.legend()
plt.show()
