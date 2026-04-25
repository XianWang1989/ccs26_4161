
# New representation for left/right
label_lr = np.zeros((N, 1), dtype=np.int_)
label_lr[l == 1] = 0  # Left
label_lr[r == 1] = 1  # Right
