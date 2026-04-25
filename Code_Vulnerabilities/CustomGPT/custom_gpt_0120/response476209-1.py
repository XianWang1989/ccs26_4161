
# Example of combining left and right labels
label_lr_combined = np.where(l > 0, 0, 1)  # Using 0 for left, 1 for right

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=label_lr_combined.astype(np.int_), **comp_kwargs)  # Combined label
