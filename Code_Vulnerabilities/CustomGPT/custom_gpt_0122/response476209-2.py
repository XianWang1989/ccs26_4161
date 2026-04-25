
import numpy as np
import caffe
from caffe import layers as L, params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    # Input Layer
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)

    # Conv Layer 1
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    # Conv Layer 2
    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    # Flatten layer
    n.flatten = L.Flatten(n.relu2)

    # Concat speed with flattened conv output
    n.join_speed = L.Concat(n.flatten, n.data_speed, axis=1)

    # Fully Connected Layer
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.relu3 = L.ReLU(n.ip1, in_place=True)

    # Output Layers
    n.ip_forward = L.InnerProduct(n.relu3, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_forward = L.SoftmaxWithLoss(n.ip_forward, n.label_forward)

    n.ip_backward = L.InnerProduct(n.relu3, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_backward = L.SoftmaxWithLoss(n.ip_backward, n.label_backward)

    n.ip_lr = L.InnerProduct(n.relu3, num_output=3, weight_filler=dict(type='xavier'))  # Adjusted for left/right/none
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
