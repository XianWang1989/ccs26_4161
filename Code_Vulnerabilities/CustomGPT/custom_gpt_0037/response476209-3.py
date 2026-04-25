
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# Load your dataset
with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_combined', data=combined_labels.astype(np.int_), **comp_kwargs)  # Combined labels

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_combined = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.relu1 = L.ReLU(n.conv1, in_place=True)
    n.pool1 = L.Pooling(n.relu1, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    n.conv2 = L.Convolution(n.pool1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.relu2 = L.ReLU(n.conv2, in_place=True)
    n.pool2 = L.Pooling(n.relu2, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    # Concatenate speed information
    n.join_speed = L.Concat(n.pool2, n.data_speed, in_place=True)

    n.ip1 = L.InnerProduct(n.join_speed, num_output=256, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    n.ip_combined = L.InnerProduct(n.sig1, num_output=4, weight_filler=dict(type='xavier'))  # Output for combined labels
    n.loss = L.SoftmaxWithLoss(n.ip_combined, n.label_combined)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
