
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

# Function to extract the cross profile
def extract_cross_profile(array, center, angle, length=50):
    x_center, y_center = center
    theta = np.radians(angle)

    # Create an array of distances along the cross profile
    distances = np.linspace(-length, length, 2 * length + 1)

    # Calculate the coordinates
    x1 = x_center + distances * np.cos(theta)
    y1 = y_center + distances * np.sin(theta)

    x2 = x_center + distances * np.cos(theta + np.pi / 2)
    y2 = y_center + distances * np.sin(theta + np.pi / 2)

    # Ensure coordinates are within bounds
    x1 = np.clip(x1, 0, array.shape[1]-1).astype(int)
    y1 = np.clip(y1, 0, array.shape[0]-1).astype(int)
    x2 = np.clip(x2, 0, array.shape[1]-1).astype(int)
    y2 = np.clip(y2, 0, array.shape[0]-1).astype(int)

    # Extract the cross profile
    profile = np.hstack((array[y1, x1], array[y2, x2]))

    return profile

# Example usage
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Plotting the cross profile
plt.plot(cross_profile)
plt.title('Cross Profile at 25 Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
