
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    # Load data
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_combined = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # CNN Layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n_relu1 = L.ReLU(n.pool1)

    n.conv2 = L.Convolution(n_relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n_relu2 = L.ReLU(n.pool2)

    n.conv3 = L.Convolution(n_relu2, kernel_size=3, num_output=128, weight_filler=dict(type='xavier'))
    n.pool3 = L.Pooling(n.conv3, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n_relu3 = L.ReLU(n.pool3)

    n.flatten = L.Flatten(n_relu3)
    n.ip1 = L.InnerProduct(n.flatten, num_output=256, weight_filler=dict(type='xavier'))
    n.relu_ip1 = L.ReLU(n.ip1)

    # Classifier for each label
    n.ip_f = L.InnerProduct(n.relu_ip1, num_output=1, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.relu_ip1, num_output=1, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    # Combined output for left/right
    n.ip_lr = L.InnerProduct(n.relu_ip1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_combined)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
