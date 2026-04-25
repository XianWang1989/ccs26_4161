
import numpy as np

# Create a 2D NumPy array representing the image (for demonstration)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the dimensions of the image
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of pixel coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
distances = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Define your function that computes the required operation
def compute_function(d, L):
    return 1 / (1 + d / L)

# Set a value for L (you can adjust this as needed)
L = np.max(distances)  # Example: using the max distance as L

# Compute the result using broadcasting, the distances calculated above
myResult = compute_function(distances, L)

# Output the results
print("Original Array:")
print(myArr)
print("\nDistance from center:")
print(distances)
print("\nResult of the function applied:")
print(myResult)
