
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Create an array to hold the profile
    profile = []

    # Calculate steps in both directions
    x_steps = np.arange(-length, length + 1)
    y_steps = np.tan(angle_rad) * x_steps

    for dx, dy in zip(x_steps, y_steps):
        x, y = x_center + dx, y_center + dy
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile.append(array[int(x), int(y)])

    return np.array(profile)

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)  # Center at (50, 50)
angle = 25         # Angle in degrees
length = 25        # Length of the profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plot the original array and the extracted profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Cross Profile')
plt.xlabel('Profile Position')
plt.ylabel('Intensity')
plt.grid()

plt.tight_layout()
plt.show()
