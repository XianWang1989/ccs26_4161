
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_lr, n.label_forward, n.label_backward = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.drop1 = L.Dropout(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.drop1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    n.conv3 = L.Convolution(n.pool2, kernel_size=5, num_output=128, weight_filler=dict(type='xavier'))
    n.pool3 = L.Pooling(n.conv3, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    n.flat = L.Flatten(n.pool3)
    n.ip1 = L.InnerProduct(n.flat, num_output=512, weight_filler=dict(type='xavier'))

    # Output for forward movement
    n.ip_f = L.InnerProduct(n.ip1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    # Output for backward movement
    n.ip_b = L.InnerProduct(n.ip1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    # Output for left or right movement
    n.ip_lr = L.InnerProduct(n.ip1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
