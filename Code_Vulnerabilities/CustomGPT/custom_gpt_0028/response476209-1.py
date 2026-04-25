
# Combine left and right labels
combined_label = np.zeros((N, 1), dtype=np.int_)
combined_label[np.where(l == 1)] = 0  # 0 for left
combined_label[np.where(r == 1)] = 1  # 1 for right
