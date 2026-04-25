
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array as an example
array = np.random.rand(100, 100)

# Function to extract the cross profile
def extract_cross_profile(arr, center, angle, length=20):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate the offsets for the diagonal lines
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Extract the coordinates for the two diagonals
    coords1 = [(int(x_center + i * dx), int(y_center + i * dy)) for i in range(-length, length+1)]
    coords2 = [(int(x_center - i * dx), int(y_center + i * dy)) for i in range(-length, length+1)]

    # Gather the values from the original array
    profile_values = [arr[y, x] if 0 <= x < arr.shape[1] and 0 <= y < arr.shape[0] else np.nan for (x, y) in coords1 + coords2]

    return profile_values

# Example usage
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Plotting the original array and the extracted cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.show()

print('Cross Profile Values:', cross_profile)
