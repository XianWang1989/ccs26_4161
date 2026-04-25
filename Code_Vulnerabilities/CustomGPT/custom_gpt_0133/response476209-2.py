
import numpy as np
import h5py

# Example: Assuming you have numpy arrays for your data
# X: input images, S: speed, f: forward, b: backward, l: left, r: right
combined_labels = np.where(l == 1, 0, 1) # Combine left and right

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_direction', data=combined_labels.astype(np.int_), **comp_kwargs)  # Combined labels

# Update CNN architecture to only use new combined label
n.ip_d = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_d = L.Accuracy(n.ip_d, n.label_direction)  # Update this line
n.loss_d = L.SoftmaxWithLoss(n.ip_d, n.label_direction)  # Update this line
