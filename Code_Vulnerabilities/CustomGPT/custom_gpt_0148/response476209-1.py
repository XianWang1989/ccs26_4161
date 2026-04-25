
# Create a single label for left/right arrow keys
combined_labels = np.where(r == 1, 1, 0) + np.where(l == 1, 2, 0)  # 0: none, 1: right, 2: left
f.create_dataset('label_direction', data=combined_labels.astype(np.int_), **comp_kwargs)
