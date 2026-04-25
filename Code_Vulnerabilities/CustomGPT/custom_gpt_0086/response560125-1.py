
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Function to extract diagonal cross profile
def extract_cross_profile(arr, center, angle, length=20):
    center_y, center_x = center
    # Calculate the slope based on the angle
    angle_rad = np.deg2rad(angle)
    slope = np.tan(angle_rad)

    # Coordinates for the cross profile
    coords = []
    for i in range(-length, length + 1):
        y1 = int(center_y + i)
        x1 = int(center_x + int(i * slope))
        y2 = int(center_y + i)
        x2 = int(center_x - int(i * slope))
        if 0 <= y1 < arr.shape[0] and 0 <= x1 < arr.shape[1]:
            coords.append(arr[y1, x1])
        if 0 <= y2 < arr.shape[0] and 0 <= x2 < arr.shape[1]:
            coords.append(arr[y2, x2])
    return np.array(coords)

# Center point and angle
center = (50, 50)
angle = 25

# Extracting the cross profile
cross_profile = extract_cross_profile(array, center, angle)
print("Cross Profile:", cross_profile)

# Optional: Visualize the array and the cross profile
plt.imshow(array, cmap='viridis', interpolation='nearest')
plt.title('2D Numpy Array')
plt.scatter(center[1], center[0], color='red', label='Center (50,50)')
plt.legend()
plt.show()
