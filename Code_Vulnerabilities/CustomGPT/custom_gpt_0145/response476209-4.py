
# HDF5 Data Preparation
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Suppose this combines left (0) and right (1)
    labels_combined = np.where(l == 1, 0, 1)  # Example mapping for left-right
    f.create_dataset('label_direction', data=labels_combined.astype(np.int_), **comp_kwargs)

# CNN Architecture Update
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_direction = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Build your CNN layers...

    # Inner Product and loss for direction
    n.ip_d = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_d = L.Accuracy(n.ip_d, n.label_direction)
    n.loss_d = L.SoftmaxWithLoss(n.ip_d, n.label_direction)

    n.loss = n.loss_f + n.loss_b + n.loss_l + n.loss_r + n.loss_d  # Final loss combination

    return n.to_proto()
