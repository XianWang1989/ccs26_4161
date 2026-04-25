
combined_labels = np.where(label_right == 1, 1, 0)

with h5py.File(train_filename, 'w') as f:
    ...
    f.create_dataset('label_side', data=combined_labels.astype(np.int_), **comp_kwargs)

# Inside the cnn function
n.ip_side = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_side = L.Accuracy(n.ip_side, n.label_side)
n.loss_side = L.SoftmaxWithLoss(n.ip_side, n.label_side)
