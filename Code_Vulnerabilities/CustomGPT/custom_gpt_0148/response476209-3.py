
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_direction = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    # Additional convolutional layers...

    # Join with speed data
    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)

    # Inner product layers
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.sig1 = L.Sigmoid(n.ip1, in_place=True)

    # Combined direction output
    n.ip_dir = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))
    n.accuracy_dir = L.Accuracy(n.ip_dir, n.label_direction)
    n.loss_dir = L.SoftmaxWithLoss(n.ip_dir, n.label_direction)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
