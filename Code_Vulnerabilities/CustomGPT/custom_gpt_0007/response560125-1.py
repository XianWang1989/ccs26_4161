
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=50):
    # Create an empty list to hold the coordinates of the cross profile
    cross_profile = []

    # Convert angle from degrees to radians
    angle_rad = np.radians(angle)

    # Calculate the direction vectors for the diagonal lines
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Calculate the coordinates for the cross profile
    for i in range(-length, length + 1):
        # Coordinates for the main diagonal
        x1 = int(center[0] + dx + i * -dy)
        y1 = int(center[1] + dy + i * dx)

        # Coordinates for the anti-diagonal
        x2 = int(center[0] + dx + i * dy)
        y2 = int(center[1] + dy - i * dx)

        # Add valid coordinates within bounds
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_profile.append(array[y1, x1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_profile.append(array[y2, x2])

    return np.array(cross_profile)

# Example of using the function
array = np.random.rand(100, 100)  # Creating a random 100x100 array
center = (50, 50)                  # Center point
angle = 25                         # Angle in degrees

# Extract the cross profile
profile = extract_cross_profile(array, center, angle)

# Display the results
print("Extracted Cross Profile:", profile)

# Optional: Visualize the results
plt.imshow(array, cmap='gray')
plt.title('2D Array')
plt.scatter([center[0], center[0] + 50 * np.cos(np.radians(angle))], 
            [center[1], center[1] + 50 * np.sin(np.radians(angle))], color='red')
plt.show()
