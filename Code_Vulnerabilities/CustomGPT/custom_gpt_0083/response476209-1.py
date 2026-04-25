
import numpy as np
import caffe
from caffe import layers as L, params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    # Load data
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_left, n.label_right = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=6)
    )

    # Convolutional layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=42, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.conv3 = L.Convolution(n.relu2, kernel_size=5, num_output=50, weight_filler=dict(type='xavier'))
    n.pool3 = L.Pooling(n.conv3, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu3 = L.ReLU(n.pool3, in_place=True)

    n.conv4 = L.Convolution(n.relu3, kernel_size=3, num_output=64, weight_filler=dict(type='xavier'))
    n.pool4 = L.Pooling(n.conv4, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu4 = L.ReLU(n.pool4, in_place=True)

    # Combining features
    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)

    # Fully connected layers
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Modify left/right labels here
    n.label_lr = L.Concat(n.label_left, n.label_right, axis=1)

    n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
