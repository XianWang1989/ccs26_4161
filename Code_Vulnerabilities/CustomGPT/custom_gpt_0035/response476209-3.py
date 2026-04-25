
n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # Adjusted output for 3 labels
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
