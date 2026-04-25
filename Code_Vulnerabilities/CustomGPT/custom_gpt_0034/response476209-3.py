
n.data_img, n.data_speed, n.label_forward, n.label_backward, n.label_lr = (
    L.HDF5Data(batch_size=batch_size, source=hdf5, ntop=5)  # updated to 5
)

# Existing layers...
# Follow the previous architecture setup

n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # for left, right, none
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
