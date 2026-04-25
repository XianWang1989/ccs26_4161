
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_combined = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # ... existing layers ...

    # Update the inner product layer for the combined labels
    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_combined)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_combined)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
