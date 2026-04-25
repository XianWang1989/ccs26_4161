
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# Create HDF5 file and dataset
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Fuse label_left and label_right
    labels_combined = np.argmax(np.array([l, r]), axis=0)  # 0 for left, 1 for right
    f.create_dataset('label_direction', data=labels_combined.astype(np.int_), **comp_kwargs)

# Update your CNN architecture
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_direction = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # (Add your convolutional and pooling layers as per your existing code)

    n.ip_r_l = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_dir = L.Accuracy(n.ip_r_l, n.label_direction)
    n.loss_dir = L.SoftmaxWithLoss(n.ip_r_l, n.label_direction)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
