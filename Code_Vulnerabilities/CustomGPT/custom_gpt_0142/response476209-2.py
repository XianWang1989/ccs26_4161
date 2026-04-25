
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# HDF5 file creation with consolidated labels
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)  # Your image data
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Example of merged left/right label:
    label_direction = np.where(l + r > 0, np.where(l > 0, 0, 1), 2)  # 0: left, 1: right, 2: none
    f.create_dataset('label_direction', data=label_direction.astype(np.int_), **comp_kwargs)

# CNN Architecture
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_direction = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.join_speed = L.Concat(n.pool1, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=128, weight_filler=dict(type='xavier'))
    n.sig1 = L.Softmax(n.ip1, in_place=True)

    # Output layer for direction
    n.ip_dir = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # 3 classes
    n.loss_dir = L.SoftmaxWithLoss(n.ip_dir, n.label_direction)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
