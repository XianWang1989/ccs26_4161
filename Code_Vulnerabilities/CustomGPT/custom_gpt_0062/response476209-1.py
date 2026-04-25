
# Modify labels for left and right arrow keys
combined_left_right = np.where(l.astype(np.int_) == 1, 0, r.astype(np.int_))  # 0 for left, 1 for right
