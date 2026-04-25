
# Combine left and right labels
n.label_lr = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=1)[0]  # New dataset for combined labels
n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # Now 3 outputs

n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
