
# Combining the left/right labels into a single label
label_lr = (l.astype(np.int_) * 2) + r.astype(np.int_)

with h5py.File(train_filename, 'w') as f:
    ...
    f.create_dataset('label_lr', data=label_lr, **comp_kwargs)
