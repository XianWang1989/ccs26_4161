
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Your convolutional layers remain unchanged...

    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Three outputs for forward, backward, and combined left-right
    n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()
