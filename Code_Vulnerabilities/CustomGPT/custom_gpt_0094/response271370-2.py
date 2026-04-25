
def transform_with_zero(vector):
    binary_matrix = np.zeros((vector.size, vector.max() + 1))
    binary_matrix[np.arange(vector.size), vector] = 1
    return binary_matrix

# Example with 0
v_with_zero = np.array([0, 1, 5, 3])
result_with_zero = transform_with_zero(v_with_zero)

print(result_with_zero)
