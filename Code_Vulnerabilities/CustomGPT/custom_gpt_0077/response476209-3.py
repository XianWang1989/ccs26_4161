
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# Example: Data Gathering
with h5py.File("train_data.h5", 'w') as f:
    f.create_dataset('data_img', data=X)  # Shape: N x K x H x W
    f.create_dataset('data_speed', data=S.astype(np.float_))  # Shape: N x 1
    combined_label = np.argmax(np.column_stack((label_left, label_right)), axis=1)
    f.create_dataset('label_lr', data=combined_label.astype(np.int_))  # Shape: N x 1

# CNN Architecture Definition
def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_lr = L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=3)

    n.conv1 = L.Convolution(n.data_img, kernel_size=7, num_output=32, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.drop1 = L.Dropout(n.pool1, in_place=True)
    n.relu1 = L.ReLU(n.drop1, in_place=True)

    # Continuing with layers...
    # (Additional layers would follow here, as per your original structure)

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # 0 for left, 1 for right
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn("train_data.h5", 100)))
