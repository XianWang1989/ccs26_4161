
# Adjusting HDF5 labels 
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combine left and right labels
    label_lr = np.vstack((l, r)).T  # Assuming l and r are arrays
    combined_lr = np.argmax(label_lr, axis=1)  # Converts to 0 or 1
    f.create_dataset('label_lr', data=combined_lr.astype(np.int_), **comp_kwargs)

    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)

# Modify the cnn function to handle the new label
n.label_lr = L.Input(n.label_lr)  # Add this line in your CNN definition
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
