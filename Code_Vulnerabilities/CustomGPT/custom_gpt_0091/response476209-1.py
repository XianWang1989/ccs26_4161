
# New label representation for left/right
label_direction = np.zeros((N, 1), dtype=np.int_)
# Assuming l and r are your left and right labels
label_direction[l == 1] = 0  # 0 for left
label_direction[r == 1] = 1  # 1 for right
