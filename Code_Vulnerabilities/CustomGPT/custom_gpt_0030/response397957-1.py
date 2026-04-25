
import numpy as np
import cv2

def calculate_distance_from_center(image_shape):
    # Get the center of the image
    center_row, center_col = (image_shape[0] - 1) / 2, (image_shape[1] - 1) / 2

    # Create an array of coordinates
    row_indices = np.arange(image_shape[0])[:, np.newaxis]  # Column vector
    col_indices = np.arange(image_shape[1])[np.newaxis, :]   # Row vector

    # Calculate the distance from the center
    distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

    return distances

def my_func(value, distance, L):
    return 1 / (1 + distance / L)

# Example usage
myArr = np.array([[0, 1, 2], [3, 4, 5]])
L = 10  # Example L value

# Calculate distances from the center
distances = calculate_distance_from_center(myArr.shape)

# Apply the function over the entire array
results = my_func(myArr, distances, L)

print("Distances:\n", distances)
print("Results:\n", results)
