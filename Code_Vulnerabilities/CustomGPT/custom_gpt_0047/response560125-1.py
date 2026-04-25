
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array for demonstration purposes
array = np.random.rand(100, 100)

# Function to extract cross profile
def extract_cross_profile(array, center, angle, length=20):
    x0, y0 = center
    # Convert angle to radians
    theta = np.radians(angle)
    # Calculate the offsets for the cross profile
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Coordinates for the cross profile
    coords = [
        (y0 + dy, x0 + dx),  # Positive slope
        (y0 - dy, x0 - dx),  # Negative slope
        (y0 + dx, x0 + dy),  # perpendicular
        (y0 - dx, x0 - dy)   # perpendicular
    ]

    profile = []
    for y, x in coords:
        if 0 <= int(y) < array.shape[0] and 0 <= int(x) < array.shape[1]:
            profile.append(array[int(y), int(x)])

    return profile

# Extract the cross profile
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

print("Cross Profile Values:", cross_profile)

# Optional: Visualizing the resulting values
plt.imshow(array, cmap='gray')
plt.scatter([50, 50], [50, 50], color='red')  # Center point
plt.title('Random Array with Center Point')
plt.show()
