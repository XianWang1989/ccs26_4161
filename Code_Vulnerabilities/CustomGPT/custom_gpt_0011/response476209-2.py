
# Updating the HDF5 creation to combine left and right labels
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combined logic for left and right labels
    # Assuming `l` and `r` are binary arrays where active key is `1`
    f.create_dataset('label_lr', data=np.where(l == 1, 0, np.where(r == 1, 1, 2)).astype(np.int_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)

# Adjusting CNN architecture to accommodate new labels
n.label_lr = n.label_left  # Adjust as needed in the net specification
# Change the output for left and right keys in architecture
n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # 0: None, 1: Left, 2: Right
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)  # Loss for the combined label
