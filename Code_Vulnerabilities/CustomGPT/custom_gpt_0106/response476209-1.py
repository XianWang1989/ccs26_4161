
# Assuming labels 'l' for left and 'r' for right
combined_label = np.where(l == 1, 0, np.where(r == 1, 1, 2))  # 0: left, 1: right, 2: neutral

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_combined', data=combined_label.astype(np.int_), **comp_kwargs)
