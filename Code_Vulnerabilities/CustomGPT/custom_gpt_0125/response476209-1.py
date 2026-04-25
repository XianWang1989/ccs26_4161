
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# Merging left and right labels into a single label
label_direction = np.where(r == 1, 1, np.where(l == 1, 0, 0))  # 0 for left, 1 for right

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_direction', data=label_direction.astype(np.int_), **comp_kwargs)

with open(train_filename_list_txt, 'w') as f:
    f.write(train_filename + '\n')

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_direction = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.drop1 = L.Dropout(n.pool1, in_place=True)
    n.relu1 = L.ReLU(n.drop1, in_place=True)

    n.ip_speed = L.InnerProduct(n.data_speed, num_output=10, weight_filler=dict(type='xavier'))

    n.join = L.Concat(n.pool1, n.ip_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Forward and backward outputs
    n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_dir = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_dir = L.SoftmaxWithLoss(n.ip_dir, n.label_direction)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
