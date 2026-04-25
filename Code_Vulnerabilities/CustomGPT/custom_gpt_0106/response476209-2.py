
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_combined = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.drop1 = L.Dropout(n.pool1, in_place=True)
    n.relu1 = L.ReLU(n.drop1, in_place=True)

    # Add more layers as necessary
    # ...

    n.fc1 = L.InnerProduct(n.relu4, num_output=3, weight_filler=dict(type='xavier'))  # Adjust for 3 outputs
    n.loss = L.SoftmaxWithLoss(n.fc1, n.label_combined)
    n.accuracy = L.Accuracy(n.fc1, n.label_combined)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
