
# Modifications for the labels in HDF5
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Fuse left and right labels
    # Here, '0' for left, '1' for right, '2' for no movement
    f.create_dataset('label_lr', data=lr.astype(np.int_), **comp_kwargs)  # Modified line

# Update CNN architecture
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)  # Adjusted ntop
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.drop1 = L.Dropout(n.pool1, in_place=True)
    n.relu1 = L.ReLU(n.drop1, in_place=True)

    # Add more layers as in your original network...

    n.sig1 = L.Sigmoid(n.ip1, in_place=True)  # Keep as you had

    # For fused labels (forward and backward)
    n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # Adjust for new num_output
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
