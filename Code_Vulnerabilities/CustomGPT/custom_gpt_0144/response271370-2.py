from scipy import sparse

def permute_matrix(vector):
    indptr = np.arange(vector.shape[0] + 1)
    ones = np.ones(vector.shape[0])
    return sparse.csr_matrix((ones, vector, indptr)).toarray()
