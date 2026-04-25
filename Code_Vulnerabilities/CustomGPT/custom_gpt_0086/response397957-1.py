
import numpy as np

# Create a sample 2D array representing your image
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Function to calculate the processing value based on distance from the center
def compute_distance_value(image, L):
    # Get the shape of the image
    h, w = image.shape

    # Calculate center coordinates
    center_row, center_col = h // 2, w // 2

    # Create coordinate grids
    row_indices = np.arange(h)[:, np.newaxis]
    col_indices = np.arange(w)[np.newaxis, :]

    # Calculate Euclidean distance from the center for each pixel
    dist = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

    # Calculate the result based on the distance
    result = 1 / (1 + dist / L)

    return result

# Parameters
L = 5  # Some constant value related to distance scaling
myResult = compute_distance_value(myArr, L)

print(myResult)
