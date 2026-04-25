
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)  # `label_lr` will be 0 for left, 1 for right
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
