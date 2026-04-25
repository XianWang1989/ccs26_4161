
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate the direction of the cross
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Prepare coordinates for the cross profile
    cross_profile = []

    for i in range(-length//2, length//2 + 1):
        # Get coordinates for the diagonal lines
        x_pos = int(x_center + i * dx)
        y_pos = int(y_center + i * dy)

        x_neg = int(x_center - i * dx)
        y_neg = int(y_center - i * dy)

        # Check boundaries and extract values
        if 0 <= x_pos < array.shape[0] and 0 <= y_pos < array.shape[1]:
            cross_profile.append(array[x_pos, y_pos])
        if 0 <= x_neg < array.shape[0] and 0 <= y_neg < array.shape[1]:
            cross_profile.append(array[x_neg, y_neg])

    return np.array(cross_profile)

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)  # Center of the cross
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Displaying results
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.grid()
plt.show()
