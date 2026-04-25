
# Assume you already have your array 'labels_lr' ready, shaped as (N, 1)
# Where labels_lr takes values:
# 0 for left (no right pressed),
# 1 for right (no left pressed),
# 2 for none pressed.

with h5py.File(train_filename, 'w') as f:
    # Your existing code...
    f.create_dataset('label_lr', data=labels_lr.astype(np.int_), **comp_kwargs)
