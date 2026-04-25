
import numpy as np
import h5py
import caffe
from caffe import layers as L
from caffe import params as P

# Assuming l and r are your label arrays for left and right key presses
# Create the fused labels where 0=left, 1=right
fused_labels = np.where(r == 1, 1, np.where(l == 1, 0, 1))

with h5py.File(train_filename, 'w') as f:
    f.create_dataset('data_img', data=X, **comp_kwargs)
    f.create_dataset('data_speed', data=S.astype(np.float_), **comp_kwargs)
    f.create_dataset('label_forward', data=f.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_backward', data=b.astype(np.int_), **comp_kwargs)
    f.create_dataset('label_lr', data=fused_labels.astype(np.int_), **comp_kwargs)  # Use the fused label dataset

def cnn(hdf5, batch_size):
    n = caffe.NetSpec()
    n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
        L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)
    )

    # Your CNN layers go here...

    n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
    n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
    n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

    return n.to_proto()

with open('cnn_train.prototxt', 'w') as f:
    f.write(str(cnn(train_filename_list_txt, 100)))
