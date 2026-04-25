
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P
import h5py

# Function to create HDF5 dataset
def create_hdf5_dataset(train_filename, X, S, f, b, l_r):
    comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
    with h5py.File(train_filename, 'w') as f:
        f.create_dataset('data_img', data=X, **comp_kwargs)
        f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

        f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
        f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
        f.create_dataset('label_lr', data=l_r.astype(np.int_), **comp_kwargs)  # Combined left/right

# CNN Architecture
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolution Layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    # Final layers
    n.join_speed = L.Concat(n.relu2, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Softmax for Output
    n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Forward
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Backward
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Left/Right
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

# Create dataset and network
train_filename = 'train_data.h5'
X = np.random.rand(1000, 3, 120, 160)  # Example image data
S = np.random.rand(1000, 1)  # Speed data
f_labels = np.random.randint(0, 2, 1000)  # Forward labels
b_labels = np.random.randint(0, 2, 1000)  # Backward labels
l_r_labels = np.random.randint(0, 2, 1000)  # Left/Right labels (0 for left, 1 for right)

create_hdf5_dataset(train_filename, X, S, f_labels, b_labels, l_r_labels)

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename, 100)))
