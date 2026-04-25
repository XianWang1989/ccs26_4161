
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_horizontal = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.drop1 = L.Dropout(n.pool1, in_place=True)
    n.relu1 = L.ReLU(n.drop1, in_place=True)

    # Rest of your architecture...

    n.ip_h = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Adjusted output
    n.accuracy_h = L.Accuracy(n.ip_h, n.label_horizontal)
    n.loss_h = L.SoftmaxWithLoss(n.ip_h, n.label_horizontal)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
