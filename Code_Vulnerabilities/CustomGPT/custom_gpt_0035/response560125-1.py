
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, width=5):
    rows, cols = array.shape
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Define the slope based on the angle
    slope = np.tan(angle_rad)

    profile = []

    for i in range(-width, width + 1):
        x1 = x_center + i
        y1 = int(y_center + slope * i)
        if 0 <= x1 < cols and 0 <= y1 < rows:
            profile.append(array[y1, x1])

        x2 = int(x_center + (width - i))
        y2 = int(y_center - slope * (width - i))
        if 0 <= x2 < cols and 0 <= y2 < rows:
            profile.append(array[y2, x2])

    return profile

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile centered at (50, 50) at 25 degrees
cross_profile = extract_cross_profile(array, (50, 50), 25)

# Plot the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.show()

plt.plot(cross_profile)
plt.title('Diagonal Cross Profile at 25 Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Intensity')
plt.show()
