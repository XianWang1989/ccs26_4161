
# Assuming your previous setup for labels already exists

# Adjust your label creation to reflect combined left/right logic
combined_label_lr = np.where(l == 1, 0, 1)  # If left pressed (1), set to 0, else 1 for right

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('label_left_right', data=combined_label_lr.astype(np.int_), **comp_kwargs)

# Update the CNN architecture in the model to accommodate combined left/right output
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_left_right = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)  # now 5 outputs
    )

    # Define the network architecture as before...

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier')) # Updated output
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_left_right) # Update for accuracy
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right) # Update loss layer for combined label

    return n.to_proto()

# Save the updated prototxt file
with open('cnn_train.prototxt', 'w') as f:
    f.write(str(
        cnn(train_filename_list_txt, 100)
    ))
