
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, width):
    rows, cols = array.shape
    x0, y0 = center
    theta = np.deg2rad(angle)

    # Calculate offsets
    dx = width * np.cos(theta)
    dy = width * np.sin(theta)

    # Generate the coordinates for the diagonal lines
    x_coords = []
    y_coords = []

    # Calculate diagonal line coordinates
    for offset in range(-width//2, width//2 + 1):
        x1 = int(x0 + offset * dy)
        y1 = int(y0 + offset * dx)

        if 0 <= x1 < rows and 0 <= y1 < cols:
            x_coords.append(x1)
            y_coords.append(y1)

        x2 = int(x0 - offset * dy)
        y2 = int(y0 - offset * dx)

        if 0 <= x2 < rows and 0 <= y2 < cols:
            x_coords.append(x2)
            y_coords.append(y2)

    # Extract the cross profile
    cross_profile = array[y_coords, x_coords]

    return cross_profile

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)
angle = 25
width = 10

cross_profile = extract_cross_profile(array, center, angle, width)

# Display the extracted cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Profile Points')
plt.ylabel('Intensity')
plt.show()
