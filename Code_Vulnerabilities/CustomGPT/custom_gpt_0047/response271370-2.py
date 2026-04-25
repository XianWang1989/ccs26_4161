
from scipy import sparse

def vector_to_sparse_binary_matrix(vector):
    # Create a sparse matrix in CSR format
    indptr = range(len(vector) + 1)
    ones = np.ones(len(vector))
    sparse_matrix = sparse.csr_matrix((ones, vector, indptr))

    return sparse_matrix.toarray()  # Convert to dense format if needed

# Example usage
sparse_result = vector_to_sparse_binary_matrix(v)
print(sparse_result)
