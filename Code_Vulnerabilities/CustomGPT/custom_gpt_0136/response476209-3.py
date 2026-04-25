
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)  # Adjusted ntop
    )

    # ... (Convolutional layers)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)  # Update accuracy for left/right
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)  # Update loss

    return n.to_proto()
