
# Assuming you already have the left and right labels as binary:
# r and l are numpy arrays representing your labels for right and left arrows
label_left_right = np.where(l == 1, 0, 1)  # 0 for left, 1 for right, assuming left is labeled as 1

# Include this new label when creating the dataset
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_left_right', data=label_left_right.astype(np.int_), **comp_kwargs)
