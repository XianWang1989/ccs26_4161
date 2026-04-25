
# Example fusion of labels
# Assuming `l` is label_left and `r` is label_right
label_lr = np.where(l == 1, 0, r)  # 0 for left arrow pressed, 1 for right arrow pressed

# Update HDF5 storage
with h5py.File(train_filename, 'w') as f:
    # ... other datasets
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)
