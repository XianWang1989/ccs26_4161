
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)

    # Combined left/right labels
    combined_lr = np.where(l > 0, 0, 1)  # 0 for left, 1 for right
    f.create_dataset('label_lr', data=combined_lr.astype(np.int_), **comp_kwargs)

    # Assuming l and r are already binary-indicators for left and right
