
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

def extract_cross_profile(arr, center, angle, length=50):
    angle_rad = np.radians(angle)

    # Calculate the deltas for the diagonal lines
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Define the two diagonal lines
    coords1 = []
    coords2 = []

    for i in range(-length, length + 1):
        x1 = center[0] + i * dy
        y1 = center[1] + i * dx

        x2 = center[0] + i * -dy
        y2 = center[1] + i * -dx

        # Append coordinates if they are within bounds
        if 0 <= int(x1) < arr.shape[0] and 0 <= int(y1) < arr.shape[1]:
            coords1.append(arr[int(x1), int(y1)])
        if 0 <= int(x2) < arr.shape[0] and 0 <= int(y2) < arr.shape[1]:
            coords2.append(arr[int(x2), int(y2)])

    return np.array(coords1), np.array(coords2)

# Extract the cross profile
center = (50, 50)
angle = 25
profile1, profile2 = extract_cross_profile(array, center, angle)

# Plot the original array and the cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Array')
plt.imshow(array, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Cross Profile')
plt.plot(profile1, label='Diagonal 1')
plt.plot(profile2, label='Diagonal 2')
plt.legend()
plt.show()
