
# Merging left and right labels
def prepare_labels(left_labels, right_labels):
    return np.where(right_labels == 1, 1, 0)  # 1 for right, 0 for left

# Sample usage
combined_labels_lr = prepare_labels(l, r)

# Save with HDF5
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_lr', data=combined_labels_lr.astype(np.int_), **comp_kwargs)
