
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Function to extract the cross profile
def extract_cross_profile(arr, center, angle, length=20):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate offsets for cross profile
    offsets = np.arange(-length, length + 1)
    x_offset = offsets * np.cos(angle_rad)
    y_offset = offsets * np.sin(angle_rad)

    # Get the coordinates of the cross profile
    cross_x = np.round(x_center + x_offset).astype(int)
    cross_y = np.round(y_center + y_offset).astype(int)

    # Extract values, ensuring we stay within boundaries
    valid_indices = (cross_x >= 0) & (cross_x < arr.shape[0]) & (cross_y >= 0) & (cross_y < arr.shape[1])
    cross_x = cross_x[valid_indices]
    cross_y = cross_y[valid_indices]

    return arr[cross_x, cross_y]

# Extract the cross profile
cross_profile = extract_cross_profile(array, (50, 50), 25)

# Display the results
plt.imshow(array, cmap='gray')
plt.scatter(cross_profile, color='red')
plt.title('Cross Profile at 25 degrees')
plt.show()
