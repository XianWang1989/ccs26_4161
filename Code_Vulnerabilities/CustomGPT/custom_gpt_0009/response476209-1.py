
# Update label structure for left/right arrow keys
n.label_lr = L.Concat(n.label_left, n.label_right, axis=1)
# Use a single output layer for left/right arrow keys
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
