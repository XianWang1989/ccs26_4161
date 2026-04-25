
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length=50):
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate the center coordinates
    x0, y0 = center

    # Calculate coordinates for the cross profile
    x1 = int(x0 + length * np.cos(theta))
    y1 = int(y0 + length * np.sin(theta))
    x2 = int(x0 - length * np.cos(theta))
    y2 = int(y0 - length * np.sin(theta))

    # Generate the cross profile points
    cross_profile = []
    for t in np.linspace(-length, length, 2 * length + 1):
        x = int(x0 + t * np.cos(theta))
        y = int(y0 + t * np.sin(theta))
        # Check bounds
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            cross_profile.append(array[x, y])

    return np.array(cross_profile)

# Extract the cross profile at (50, 50) with a 25-degree angle
cross_profile = extract_cross_profile(array, center=(50, 50), angle=25)

# Plot the original array and the extracted cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Cross Profile at 25°')
plt.xlabel('Distance from Center')
plt.ylabel('Value')
plt.grid()
plt.show()
