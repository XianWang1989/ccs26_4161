
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 2D NumPy array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length=20):
    # Get the center coordinates
    x_center, y_center = center
    # Calculate the slope of the line from the angle
    slope = np.tan(np.radians(angle))

    # Initialize lists to hold the diagonal values
    cross_values = []

    # Extract points from the cross profile
    for i in range(-length, length + 1):
        # Calculate the x and y coordinates for the diagonal
        x1 = x_center + i
        y1 = y_center + int(i * slope)

        x2 = x_center + int(i / slope)
        y2 = y_center + i

        # Ensure we stay within bounds
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_values.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_values.append(array[x2, y2])

    return cross_values

# Define the center and angle
center = (50, 50)
angle = 25

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle)

# Plot the original array and the extracted cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()
plt.show()

plt.plot(cross_profile)
plt.title('Diagonal Cross Profile at 25 Degrees')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid()
plt.show()
