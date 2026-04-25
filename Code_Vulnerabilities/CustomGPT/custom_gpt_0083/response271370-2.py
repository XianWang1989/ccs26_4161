
def permute_array_adjusted(vector):
    # Adjust the vector by adding 1 to handle zero indexing
    adjusted_vector = vector + 1
    permut = np.zeros((vector.shape[0], adjusted_vector.max() + 1))
    permut[np.arange(vector.shape[0]), adjusted_vector] = 1
    return permut

# Example usage
v = np.array([0, 4, 2])
result = permute_array_adjusted(v)
print(result)
