
import numpy as np

def extract_cross_profile(arr, center, angle, length):
    x0, y0 = center
    angle_rad = np.radians(angle)

    # Calculate deltas based on angle
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Generate coordinates along the diagonal
    coords = []
    for i in range(-length // 2, length // 2 + 1):
        x = int(x0 + i * dx)
        y = int(y0 + i * dy)
        if 0 <= x < arr.shape[0] and 0 <= y < arr.shape[1]:
            coords.append(arr[y, x])

    return np.array(coords)

# Example usage
array_2d = np.random.rand(100, 100)  # Create a 100x100 random array
cross_profile = extract_cross_profile(array_2d, center=(50, 50), angle=25, length=20)
print(cross_profile)
