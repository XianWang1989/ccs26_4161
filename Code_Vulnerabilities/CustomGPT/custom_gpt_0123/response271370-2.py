
from scipy import sparse

def transform_to_sparse_matrix(vector):
    ones = np.ones(len(vector))
    indices = vector
    indptr = range(len(vector) + 1)

    sparse_matrix = sparse.csr_matrix((ones, indices, indptr), shape=(len(vector), vector.max() + 1))
    return sparse_matrix.toarray()

# Example usage
C_sparse = transform_to_sparse_matrix(v)
print(C_sparse)
