
from scipy import sparse

def permute_sparse(vector):
    # Create a sparse matrix from the indices
    indptr = range(len(vector) + 1)
    ones = np.ones(len(vector))
    permut = sparse.csr_matrix((ones, vector, indptr))
    return permut.toarray()

# Example usage
v = np.random.randint(0, 1000, size=1000)
sparse_result = permute_sparse(v)
print(sparse_result)
