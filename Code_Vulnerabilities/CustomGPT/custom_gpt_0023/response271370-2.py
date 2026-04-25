
from scipy import sparse

def transform_to_sparse_matrix(v):
    indptr = np.arange(len(v) + 1)
    ones = np.ones(len(v))
    sparse_matrix = sparse.csr_matrix((ones, v, indptr), shape=(len(v), v.max() + 1))
    return sparse_matrix.toarray()

# Example usage for sparse
sparse_binary_matrix = transform_to_sparse_matrix(v)
print(sparse_binary_matrix)
