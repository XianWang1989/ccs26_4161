
# Convert left and right labels to a combined label
label_lr_combined = np.where(l.astype(np.int_) == 1, 0, 1)  # 0 for left, 1 for right

# Save this combined label in the dataset
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_lr', data=label_lr_combined.astype(np.int_), **comp_kwargs)
