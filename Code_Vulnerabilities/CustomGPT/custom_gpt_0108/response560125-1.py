
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate the offsets for the diagonal lines
    x_offset = np.arange(-length, length + 1)
    y_offset = np.tan(angle_rad) * x_offset

    # Calculate the first diagonal (positive slope)
    coords1 = [(x_center + x, y_center + y) for x, y in zip(x_offset, y_offset)]
    coords1 = [(x, y) for x, y in coords1 if 0 <= x < cols and 0 <= y < rows]

    # Calculate the second diagonal (negative slope)
    y_offset_neg = -y_offset
    coords2 = [(x_center + x, y_center + y) for x, y in zip(x_offset, y_offset_neg)]
    coords2 = [(x, y) for x, y in coords2 if 0 <= x < cols and 0 <= y < rows]

    # Combine coordinates and extract values
    coords = coords1 + coords2
    extracted_values = [array[y, x] for x, y in coords]

    return extracted_values

# Example usage
np.random.seed(0)
array = np.random.rand(100, 100)  # Random 100x100 array
center = (50, 50)
angle = 25
length = 20

cross_profile = extract_cross_profile(array, center, angle, length)

# Display results
print(cross_profile)

# Optional: visualize the array and the cross section
plt.imshow(array, cmap='gray')
plt.scatter([center[0]], [center[1]], color='red')  # Center point
plt.title('Array with Center Point')
plt.show()
