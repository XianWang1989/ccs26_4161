
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_lr, n.label_backward = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=4)
    )

    # Your convolutional layers as before...

    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # Forward, Backward, Left/Right
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(
        cnn(train_filename_list_txt, 100)
    ))
