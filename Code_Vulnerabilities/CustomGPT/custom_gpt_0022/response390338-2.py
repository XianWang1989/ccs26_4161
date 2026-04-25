
def swap_rb(mat):
    X = mat[:,:,2].copy()
    mat[:,:,2] = mat[:,:,0]
    mat[:,:,0] = X
    return mat
