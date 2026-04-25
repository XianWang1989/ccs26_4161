
# Combined label creation example
# Example assumes labels are loaded as arrays from your dataset
# where `l` and `r` are previously defined as labels for left and right keys

label_combined = np.where(r == 1, 1, 0)  # 1 if right, 0 if left

# Modify dataset creation in HDF5 to include combined label
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_left_right', data=label_combined.astype(np.int_), **comp_kwargs)

# CNN Layer changes for combined left/right output
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_left_right)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right)

# Update the network structure
return n.to_proto()
