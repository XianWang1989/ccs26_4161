
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_horizontal = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.drop1 = L.Dropout(n.relu2, in_place=True)

    n.flatten = L.Flatten(n.drop1)

    n.ip1 = L.InnerProduct(n.flatten, num_output=512, weight_filler=dict(type='xavier'))
    n.relu3 = L.ReLU(n.ip1, in_place=True)
    n.drop2 = L.Dropout(n.relu3, in_place=True)

    n.ip_f = L.InnerProduct(n.drop2, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.drop2, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    n.ip_h = L.InnerProduct(n.drop2, num_output=3, weight_filler=dict(type='xavier')) # 0:left, 1:right, 2:none
    n.loss_h = L.SoftmaxWithLoss(n.ip_h, n.label_horizontal)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
