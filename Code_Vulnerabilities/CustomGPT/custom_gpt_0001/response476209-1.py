
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# Data preparation in HDF5
# Assuming you have defined and populated labels accordingly
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)

    # Combined left/right labels
    f.create_dataset('label_direction', data=direction_labels.astype(np.int_), **comp_kwargs)

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_direction = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.join_speed = L.Concat(n.relu2, n.data_speed, in_place=True)
    n.ip_direction = L.InnerProduct(n.join_speed, num_output=2, weight_filler=dict(type='xavier'))

    n.loss = L.SoftmaxWithLoss(n.ip_direction, n.label_direction)
    n.accuracy = L.Accuracy(n.ip_direction, n.label_direction)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
