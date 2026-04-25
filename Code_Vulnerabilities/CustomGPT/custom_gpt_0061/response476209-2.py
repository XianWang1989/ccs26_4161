
# Merging left and right labels
label_left_right = np.where(l + r > 0, np.where(l > r, 0, 1), 2)  # 0 for left, 1 for right, 2 for none
f.create_dataset('label_left_right', data=label_left_right.astype(np.int_), **comp_kwargs)
