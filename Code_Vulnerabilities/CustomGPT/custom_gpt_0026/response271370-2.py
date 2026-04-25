
from scipy import sparse

def sparse_transform_to_binary_matrix(vector):
    indptr = range(len(vector) + 1)
    ones = np.ones(len(vector))
    sparse_matrix = sparse.csr_matrix((ones, vector, indptr), shape=(len(vector), vector.max() + 1))
    return sparse_matrix.toarray()

# Example usage
sparse_result = sparse_transform_to_binary_matrix(v)
print(sparse_result)
