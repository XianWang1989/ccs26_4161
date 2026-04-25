
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional Layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=42, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    # Further Convolutions...
    n.conv4 = L.Convolution(n.relu3, kernel_size=3, num_output=64, weight_filler=dict(type='xavier'))
    n.pool4 = L.Pooling(n.conv4, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    # Joining Layers
    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)

    # Inner Product Layers for Output
    n.ip_f = L.InnerProduct(n.join_speed, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)  # Forward label

    n.ip_b = L.InnerProduct(n.join_speed, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)  # Backward label

    n.ip_lr = L.InnerProduct(n.join_speed, num_output=3, weight_filler=dict(type='xavier'))  # Combined for left/right
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()
