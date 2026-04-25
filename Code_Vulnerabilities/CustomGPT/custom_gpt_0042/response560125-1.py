
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Calculate the step size based on the angle in radians
    theta = np.radians(angle)
    x_step = np.cos(theta)
    y_step = np.sin(theta)

    # Store the coordinates of the cross profile
    profile = []

    # Generate points along the profile
    for i in range(-length//2, length//2 + 1):
        x = int(center[0] + i * x_step)
        y = int(center[1] + i * y_step)
        # Ensure indices are within the bounds of the array
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile.append(array[x, y])

    return np.array(profile)

# Create a sample 100x100 array
data = np.random.rand(100, 100)

# Parameters
center = (50, 50)   # Center point
angle = 25          # Angle in degrees
length = 20         # Length of the cross profile

# Extract cross profile
cross_profile = extract_cross_profile(data, center, angle, length)

# Print the cross profile
print("Cross Profile:", cross_profile)

# Optional: Visualize the data and the cross profile line
plt.imshow(data, cmap='viridis')
plt.colorbar()

# Overlay the cross profile on the plot
plt.plot(center[1] + np.arange(-length//2, length//2 + 1) * np.sin(np.radians(angle)), 
         center[0] + np.arange(-length//2, length//2 + 1) * np.cos(np.radians(angle)), 
         color='red')
plt.scatter(center[1], center[0], color='white')  # Mark the center point
plt.title('Cross Profile Extraction')
plt.show()
