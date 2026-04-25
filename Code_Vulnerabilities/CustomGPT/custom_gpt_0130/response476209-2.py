
# Adjusting the label creation
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_lr', data=np.where(l > r, 0, 1).astype(np.int_), **comp_kwargs)

# Modify your CNN to include the new label
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional layers...

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()
