
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, width=5):
    rows, cols = array.shape
    x_center, y_center = center

    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate the direction vectors
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Generate offsets for cross profile
    offsets = np.linspace(-width, width, 2 * width + 1)

    # Extract points along the angle
    profile_values = []
    for offset in offsets:
        x1 = int(x_center + offset * dy)  # Perpendicular slope for one direction
        y1 = int(y_center + offset * dx)
        x2 = int(x_center - offset * dy)  # Perpendicular slope for the other direction
        y2 = int(y_center - offset * dx)

        # Ensure indices are within bounds
        if 0 <= x1 < rows and 0 <= y1 < cols:
            profile_values.append(array[x1, y1])
        if 0 <= x2 < rows and 0 <= y2 < cols and (x2, y2) != (x1, y1):
            profile_values.append(array[x2, y2])

    return np.array(profile_values)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Print and plot the result
print(cross_profile)

# Plotting for visualization
plt.plot(cross_profile)
plt.title("Diagonal Cross Profile at 25 Degrees")
plt.xlabel("Offset")
plt.ylabel("Value")
plt.show()
