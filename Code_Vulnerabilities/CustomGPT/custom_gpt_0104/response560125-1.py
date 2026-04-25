
import numpy as np

def extract_cross_profile(array, center, angle, length=10):
    """ Extract a diagonal cross profile from a 2D numpy array based on center and angle. """
    # Convert angle to radians
    radians = np.radians(angle)

    # Calculate the direction vectors
    dx = np.cos(radians)
    dy = np.sin(radians)

    # Initialize lists to hold the indices
    indices_positive = []
    indices_negative = []

    # Calculate points in both diagonals (positive and negative)
    for i in range(-length, length + 1):
        x_pos = int(center[0] + i * dx)
        y_pos = int(center[1] + i * dy)
        x_neg = int(center[0] + i * dy)
        y_neg = int(center[1] - i * dx)

        # Ensure indices are within bounds
        if 0 <= x_pos < array.shape[0] and 0 <= y_pos < array.shape[1]:
            indices_positive.append(array[x_pos, y_pos])

        if 0 <= x_neg < array.shape[0] and 0 <= y_neg < array.shape[1]:
            indices_negative.append(array[x_neg, y_neg])

    return indices_positive, indices_negative

# Sample usage
array = np.random.rand(100, 100)  # create a random 100x100 array
center = (50, 50)
angle = 25

positive_diagonal, negative_diagonal = extract_cross_profile(array, center, angle, length=10)

print("Positive Diagonal:", positive_diagonal)
print("Negative Diagonal:", negative_diagonal)
