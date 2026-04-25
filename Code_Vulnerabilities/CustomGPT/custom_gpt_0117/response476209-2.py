
import caffe
from caffe import layers as L
from caffe import params as P

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()

    # Load data
    n.data_img, n.data_speed, n.label_dir, n.label_forward, n.label_backward = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Convolutional layers
    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu1 = L.ReLU(n.pool1, in_place=True)

    n.conv2 = L.Convolution(n.relu1, kernel_size=5, num_output=64, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.relu2 = L.ReLU(n.pool2, in_place=True)

    n.flatten = L.Flatten(n.relu2)

    # Combine speed and flattened output
    n.join_speed = L.Concat(n.flatten, n.data_speed, axis=1, in_place=False)

    # Fully connected layers
    n.fc1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
    n.relu_fc1 = L.ReLU(n.fc1, in_place=True)

    n.fc_forward = L.InnerProduct(n.relu_fc1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_forward = L.SoftmaxWithLoss(n.fc_forward, n.label_forward)

    n.fc_backward = L.InnerProduct(n.relu_fc1, num_output=2, weight_filler=dict(type='xavier'))
    n.loss_backward = L.SoftmaxWithLoss(n.fc_backward, n.label_backward)

    n.fc_direction = L.InnerProduct(n.relu_fc1, num_output=3, weight_filler=dict(type='xavier'))  # 0: left, 1: right, 2: none
    n.loss_direction = L.SoftmaxWithLoss(n.fc_direction, n.label_dir)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
