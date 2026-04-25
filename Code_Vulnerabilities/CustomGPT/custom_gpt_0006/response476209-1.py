
# Merging label_left and label_right
label_lr = np.where(l == 1, 0, 1)  # 0 for left, 1 for right if left is pressed
# Save to HDF5
f.create_dataset('label_left_right', data=label_lr.astype(np.int_), **comp_kwargs)
