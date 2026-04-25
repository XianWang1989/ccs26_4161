
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_combined = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Your existing convolutional structure
    # ...

    n.ip_combined = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_combined = L.Accuracy(n.ip_combined, n.label_combined)
    n.loss_combined = L.SoftmaxWithLoss(n.ip_combined, n.label_combined)

    return n.to_proto()
