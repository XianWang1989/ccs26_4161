
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 2D array
array = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(array, center, angle, length=20):
    row, col = center
    angle_rad = np.deg2rad(angle)

    # Calculate the end points of the cross profile
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Generate coordinates for the cross profile
    x1, y1 = int(col - dx), int(row - dy)
    x2, y2 = int(col + dx), int(row + dy)

    # Ensure coordinates are within bounds
    x1 = max(0, min(x1, array.shape[1]-1))
    y1 = max(0, min(y1, array.shape[0]-1))
    x2 = max(0, min(x2, array.shape[1]-1))
    y2 = max(0, min(y2, array.shape[0]-1))

    # Extract the cross profile
    cross_profile = []
    for i in range(max(x1, 0), min(x2 + 1, array.shape[1])):
        j = int(row + (i - col) * dy / dx) if dx != 0 else row
        if 0 <= j < array.shape[0]:
            cross_profile.append(array[j, i])

    return np.array(cross_profile)

# Example usage
center = (50, 50)
angle = 25
profile = extract_cross_profile(array, center, angle)

# Plot the original array and the extracted profile
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.title("Original Array")
plt.imshow(array, cmap='gray')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title("Diagonal Cross Profile")
plt.plot(profile)
plt.xlabel("Profile Length")
plt.ylabel("Value")
plt.grid()

plt.show()
