
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(array, center, angle, length=20):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate coordinates for the cross profile
    delta_x = np.arange(-length, length + 1)
    delta_y = np.tan(angle_rad) * delta_x

    # Calculate diagonal coordinates
    diag_coords1 = (x_center + delta_x, y_center + delta_y)
    diag_coords2 = (x_center - delta_y / np.tan(angle_rad), y_center + delta_x)

    # Extract values
    profile1 = []
    profile2 = []
    for x, y in zip(*diag_coords1):
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile1.append(array[int(x), int(y)])

    for x, y in zip(*diag_coords2):
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile2.append(array[int(x), int(y)])

    return np.array(profile1), np.array(profile2)

# Define center and angle
center = (50, 50)
angle = 25

# Extract the cross profile
profile1, profile2 = extract_cross_profile(array, center, angle)

# Display the profiles
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(profile1, label='Diagonal 1')
plt.title('Profile 1')
plt.xlabel('Offset')
plt.ylabel('Value')

plt.subplot(1, 2, 2)
plt.plot(profile2, label='Diagonal 2')
plt.title('Profile 2')
plt.xlabel('Offset')
plt.ylabel('Value')

plt.tight_layout()
plt.show()
