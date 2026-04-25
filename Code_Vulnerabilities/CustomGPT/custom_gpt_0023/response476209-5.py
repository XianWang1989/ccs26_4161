
# Adjusting label storage
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_combined', data=combined_labels.astype(np.int_), **comp_kwargs)

# Network definition with combined output
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_combined = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)

    # Convolutional layers (unchanged for brevity)
    # ...

    # Combined output layer
    n.ip_all = L.InnerProduct(n.join_speed, num_output=4, weight_filler=dict(type='xavier'))
    n.loss_all = L.SoftmaxWithLoss(n.ip_all, n.label_combined)

    return n.to_proto()
