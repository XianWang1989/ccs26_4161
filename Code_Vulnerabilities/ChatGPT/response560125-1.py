
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=10):
    row, col = center
    angle_rad = np.radians(angle)

    # Calculate direction vectors for the two lines forming the cross
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Creating offsets for the line along the angle
    offsets = np.arange(-length, length + 1)

    # Generate coordinates for both directions of the cross
    points1 = [(row + dy * offset, col + dx * offset) for offset in offsets]
    points2 = [(row - dy * offset, col - dx * offset) for offset in offsets]

    # Combine both sets of points
    points = points1 + points2

    # Extract values from the array for valid points
    cross_values = []

    for r, c in points:
        if 0 <= int(r) < array.shape[0] and 0 <= int(c) < array.shape[1]:
            cross_values.append(array[int(r), int(c)])

    return np.array(cross_values)

# Example usage
array = np.random.random((100, 100)) # Create a random 100x100 array
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Display the cross profile
print("Cross Profile Values:", cross_profile)

# Optional: Visualize the original array and the line
plt.figure(figsize=(8, 8))
plt.imshow(array, cmap='gray')
for i in range(len(cross_profile)):
    row, col = 50 + np.round(np.sin(np.radians(angle)) * (i - 10)), 50 + np.round(np.cos(np.radians(angle)) * (i - 10))
    plt.plot(col, row, 'ro')  # Marking the points of the cross profile
plt.scatter(*center[::-1], color='blue')  # Mark the center
plt.title('Cross Profile Extraction')
plt.show()
