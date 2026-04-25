
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_horizontal, n.label_vertical = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=4)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    #... (additional layers unchanged)

    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)

    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Horizontal movement classification
    n.ip_h = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Left/Right
    n.loss_h = L.SoftmaxWithLoss(n.ip_h, n.label_horizontal)

    # Vertical movement classification
    n.ip_v = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Forward/Backward
    n.loss_v = L.SoftmaxWithLoss(n.ip_v, n.label_vertical)

    return n.to_proto()
