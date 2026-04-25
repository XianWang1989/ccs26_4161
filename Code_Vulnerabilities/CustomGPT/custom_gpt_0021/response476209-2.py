
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_direction = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.conv3 = L.Convolution(n.relu2, kernel_size=3, num_output=128, weight_filler=dict(type='xavier'))
    n.pool3 = L.Pooling(n.conv3, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu3 = L.ReLU(n.pool3, in_place=True)

    n.flatten = L.Flatten(n.relu3)
    n.join_speed = L.Concat(n.flatten, n.data_speed, in_place=True)

    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.relu_ip1 = L.ReLU(n.ip1, in_place=True)

    # Adjusted to use a combined label for left/right
    n.ip_direction = L.InnerProduct(n.relu_ip1, num_output=3, weight_filler=dict(type='xavier'))
    n.loss_direction = L.SoftmaxWithLoss(n.ip_direction, n.label_direction)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
