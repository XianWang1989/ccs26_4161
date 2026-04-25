
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate the direction vectors
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Create coordinates for the central point
    cross_profile = []

    for i in range(-length//2, length//2 + 1):
        # Calculate new coordinates
        x = int(x_center + i * dy)  # Switch dy and dx to get the cross direction
        y = int(y_center + i * dx)  # Switch dx and dy for proper angle alignment
        # Check bounds and append if within range
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            cross_profile.append(array[x, y])

    return np.array(cross_profile)

# Extract a cross profile of length 50 at (50,50) with an angle of 25 degrees
cross_section = extract_cross_profile(array, (50, 50), 25, 50)

# Display results
print("Cross Profile Values:", cross_section)

# Optional: Visualize the original array and the extracted profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()
plt.show()
