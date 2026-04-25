
# Adjusted output layer for left/right keys
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
