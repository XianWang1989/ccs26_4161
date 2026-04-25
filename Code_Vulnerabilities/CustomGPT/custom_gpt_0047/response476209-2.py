
# Before this, ensure you set conditions for the combined label
label_lr = np.zeros(N)  # Shape (N,)
label_lr[condition_for_left] = 0  # Left pressed
label_lr[condition_for_right] = 1  # Right pressed

# Store in HDF5
with h5py.File(train_filename, 'w') as f:
    ...
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)

# Modify net specification
n.label_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.label_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.label_lr, n.label_lr)
