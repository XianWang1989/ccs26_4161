
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array (example data)
array = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(arr, center, angle, length=20):
    # Convert degrees to radians
    radians = np.radians(angle)

    # Calculate the step sizes based on the angle
    dx = np.cos(radians)
    dy = np.sin(radians)

    # Initialize lists to hold the x and y coordinates
    x_coords = []
    y_coords = []

    # Calculate coordinates in both directions from the center
    for d in range(-length, length + 1):
        x1 = int(center[0] + d * dx)
        y1 = int(center[1] + d * dy)
        x2 = int(center[0] + d * -dx)
        y2 = int(center[1] + d * -dy)

        # Append coordinates if they're within bounds
        if 0 <= x1 < arr.shape[0] and 0 <= y1 < arr.shape[1]:
            x_coords.append(x1)
            y_coords.append(y1)
        if 0 <= x2 < arr.shape[0] and 0 <= y2 < arr.shape[1]:
            x_coords.append(x2)
            y_coords.append(y2)

    # Extract the values from the array
    profile_values = [arr[y, x] for x, y in zip(x_coords, y_coords) if 0 <= x < arr.shape[0] and 0 <= y < arr.shape[1]]

    return np.array(profile_values)

# Center point and angle
center_point = (50, 50)
angle = 25

# Extract the cross profile
cross_profile = extract_cross_profile(array, center_point, angle)

# Print the extracted profile
print(cross_profile)

# Optional: Visualize the original array and the extracted profile
plt.imshow(array, cmap='gray', interpolation='nearest')
plt.title('Original 2D Array')
plt.colorbar()
plt.show()
