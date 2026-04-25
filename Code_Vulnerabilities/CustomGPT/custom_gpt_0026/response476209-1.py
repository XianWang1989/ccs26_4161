
# Combined left/right label
label_lr = np.where(l.astype(np.int_) == 1, 0, 1)  # 0 for left, 1 for right

with h5py.File(train_filename, 'w') as f:
    # Other datasets...
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)
