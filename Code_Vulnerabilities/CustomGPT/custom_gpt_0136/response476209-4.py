
# Example code to process labels and adjust the network
import h5py
import numpy as np

# Assuming you have loaded your images X and speed S
label_lr = np.where(l == 1, 0, r)  # 0 for left, 1 for right

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=label_lr.astype(np.int_), **comp_kwargs)

# Train the network with the revised architecture
with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
