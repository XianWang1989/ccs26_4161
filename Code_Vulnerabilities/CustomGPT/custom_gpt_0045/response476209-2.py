
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_arrows = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)
    )

    # The rest of the layers (conv1 through drop4) remain unchanged...

    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    n.ip_arrows = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # Updated for combined labels
    n.loss_arrows = L.SoftmaxWithLoss(n.ip_arrows, n.label_arrows)  # Updated to handle combined label

    n.accuracy_arrows = L.Accuracy(n.ip_arrows, n.label_arrows)  # Updated to handle combined label

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
