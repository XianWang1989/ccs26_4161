
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_combined = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=42, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.conv3 = L.Convolution(n.relu2, kernel_size=5, num_output=50, weight_filler=dict(type='xavier'))
    n.pool3 = L.Pooling(n.conv3, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu3 = L.ReLU(n.pool3, in_place=True)

    n.pool4 = L.Pooling(n.relu3, kernel_size=2, stride=2, pool=P.Pooling.AVE)

    n.join_speed = L.Concat(n.pool4, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    n.ip_combined = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # 3 for the combined outputs
    n.loss_combined = L.SoftmaxWithLoss(n.ip_combined, n.label_combined)

    return n.to_proto()

# Writing to the prototxt
with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
