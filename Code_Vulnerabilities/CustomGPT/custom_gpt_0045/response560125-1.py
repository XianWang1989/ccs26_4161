
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D numpy array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate the slope for both diagonal lines
    slope_positive = np.tan(angle_rad)
    slope_negative = -slope_positive

    # Initialize lists to hold the diagonal coordinates
    coords_positive = []
    coords_negative = []

    for d in range(-length//2, length//2 + 1):
        # Coordinates for the positive diagonal
        x_pos = x_center + d
        y_pos = y_center + int(slope_positive * d)

        # Coordinates for the negative diagonal
        x_neg = x_center + d
        y_neg = y_center + int(slope_negative * d)

        # Check if the coordinates are within bounds
        if 0 <= x_pos < array.shape[0] and 0 <= y_pos < array.shape[1]:
            coords_positive.append(array[x_pos, y_pos])

        if 0 <= x_neg < array.shape[0] and 0 <= y_neg < array.shape[1]:
            coords_negative.append(array[x_neg, y_neg])

    return np.array(coords_positive), np.array(coords_negative)

# Define the parameters
center = (50, 50)     # Center of the cross profile
angle = 25            # Angle in degrees
length = 30           # Length of the cross profile

# Extract cross profiles
positive_diag, negative_diag = extract_cross_profile(array, center, angle, length)

# Display results
print("Positive Diagonal Profile:", positive_diag)
print("Negative Diagonal Profile:", negative_diag)

# Optional: Visualization
plt.plot(positive_diag, label='Positive Diagonal')
plt.plot(negative_diag, label='Negative Diagonal')
plt.title('Diagonal Cross Profile')
plt.xlabel('Samples')
plt.ylabel('Intensity')
plt.legend()
plt.show()
