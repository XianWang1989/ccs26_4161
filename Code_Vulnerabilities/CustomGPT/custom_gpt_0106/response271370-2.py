
def transform_to_binary_matrix(vector):
    rows = vector.shape[0]
    cols = vector.max() + 1  # Ensures enough columns
    binary_matrix = np.zeros((rows, cols))

    binary_matrix[np.arange(rows), vector] = 1  # Direct indexing

    return binary_matrix
