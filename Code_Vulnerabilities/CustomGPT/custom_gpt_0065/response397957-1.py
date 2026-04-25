
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Function to calculate distance and apply the transformation
def calculate_distance(myArr, L):
    # Get the shape of the array
    rows, cols = myArr.shape
    # Calculate the center coordinates
    center_row, center_col = rows // 2, cols // 2

    # Create a grid of coordinates
    y_indices, x_indices = np.indices(myArr.shape)

    # Calculate the euclidean distance from the center
    distances = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

    # Apply the function
    result = 1 / (1 + distances / L)

    return result

# Set the parameter L
L = 10  # Example value

# Call the function
myResult = calculate_distance(myArr, L)

print(myResult)
