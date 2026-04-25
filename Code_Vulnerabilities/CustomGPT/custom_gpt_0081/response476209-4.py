
import numpy as np
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_left_right = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional Layers as defined earlier...
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    # ... (rest of convolutional layers as before)

    # Combine data and speed for the fully connected layer
    n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)
    n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))

    # Outputs for forward/backward movement
    n.ip_f = L.InnerProduct(n.ip1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

    n.ip_b = L.InnerProduct(n.ip1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

    # Output for left/right movement (0: none, 1: left, 2: right)
    n.ip_lr = L.InnerProduct(n.ip1, num_output=3, weight_filler=dict(type='xavier'))
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
