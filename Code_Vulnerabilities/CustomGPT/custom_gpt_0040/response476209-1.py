
# Assuming the following encoding for combined labels
# Forward = 1, Backward = 2, Left = 3, Right = 4, None = 0
combined_labels = np.zeros((N, 1), dtype=np.int_)
combined_labels[forward_indices] = 1
combined_labels[backward_indices] = 2
combined_labels[left_indices] = 3
combined_labels[right_indices] = 4

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('labels', data=combined_labels, **comp_kwargs)
