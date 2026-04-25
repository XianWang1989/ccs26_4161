
n.label_direction = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=1)

# Change the inner product layer for direction prediction
n.ip_d = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_d = L.Accuracy(n.ip_d, n.label_direction)
n.loss_d = L.SoftmaxWithLoss(n.ip_d, n.label_direction)
