
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(arr, center, angle, length):
    y, x = center
    angle_rad = np.radians(angle)

    # Calculate the offsets for the cross profile
    offsets = np.arange(-length // 2, length // 2 + 1)

    # Diagonal indices
    diag_x1 = x + offsets * np.cos(angle_rad)
    diag_y1 = y + offsets * np.sin(angle_rad)
    diag_x2 = x + offsets * np.cos(angle_rad + np.pi / 2)
    diag_y2 = y + offsets * np.sin(angle_rad + np.pi / 2)

    # Extracting values within bounds
    cross_profile = []
    for dx, dy in zip(np.round(diag_x1).astype(int), np.round(diag_y1).astype(int)):
        if 0 <= dx < arr.shape[1] and 0 <= dy < arr.shape[0]:
            cross_profile.append(arr[dy, dx])

    for dx, dy in zip(np.round(diag_x2).astype(int), np.round(diag_y2).astype(int)):
        if 0 <= dx < arr.shape[1] and 0 <= dy < arr.shape[0]:
            cross_profile.append(arr[dy, dx])

    return cross_profile

# Extract the cross profile
cross_profile = extract_cross_profile(array, (50, 50), 25, 20)

# Display results
print("Cross Profile Values:", cross_profile)

# Optional: Visualize the original array and cross profile
plt.imshow(array, cmap='gray')
plt.scatter([50], [50], c='red', label='Center (50, 50)', s=100)
plt.title('Original Array')
plt.colorbar()
plt.legend()
plt.show()
