
import numpy as np

# Create a 2D numpy array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Function to compute the distance based on the coordinates
def compute_distance(image, L):
    # Get the dimensions of the image
    rows, cols = image.shape
    center_row, center_col = rows / 2, cols / 2

    # Create meshgrid for row and column indices
    row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

    # Calculate the Euclidean distance from the center
    d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

    # Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
    result = 1 / (1 + d / L)

    return result

# Example usage
L = 2  # Scaling factor
myResult = compute_distance(myArr, L)

print(myResult)
