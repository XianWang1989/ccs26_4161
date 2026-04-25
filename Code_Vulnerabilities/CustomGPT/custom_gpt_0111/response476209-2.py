
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    # Input layers
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_left_right = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional layers with pooling and activation
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.conv3 = L.Convolution(n.relu2, kernel_size=5, num_output=128, weight_filler=dict(type='xavier'))
    n.pool3 = L.Pooling(n.conv3, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu3 = L.ReLU(n.pool3, in_place=True)

    n.conv4 = L.Convolution(n.relu3, kernel_size=3, num_output=256, weight_filler=dict(type='xavier'))
    n.pool4 = L.Pooling(n.conv4, kernel_size=3, stride=2, pool=P.Pooling.AVE)

    # Concatenation layer
    n.join_speed = L.Concat(n.relu4, n.data_speed, axis=1)  # Concatenate along the channel dimension
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Output layers for each action
    n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Left/Right fusion
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
