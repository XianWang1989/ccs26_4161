
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    # Load data
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=42, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.drop2 = L.Dropout(n.relu2, in_place=True)

    n.join_speed = L.Concat(n.drop2, n.data_speed, in_place=True)

    n.ip_f = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip_f, in_place=True)

    # Output for forward and backward
    n.ip_forward = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_forward = L.SoftmaxWithLoss(n.ip_forward, n.label_forward)

    n.ip_backward = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_backward = L.SoftmaxWithLoss(n.ip_backward, n.label_backward)

    # Merged Output for Left/Right
    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
