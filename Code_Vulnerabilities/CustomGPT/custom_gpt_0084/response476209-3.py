
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_left_right = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # [Convolutional layers remain unchanged]

    n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_f = L.Accuracy(n.ip_f, n.label_forward)
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_b = L.Accuracy(n.ip_b, n.label_backward)
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # For left/right
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_left_right)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right)

    return n.to_proto()
