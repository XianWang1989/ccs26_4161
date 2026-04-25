
# Fusion of left/right labels into a single output
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, L.Concat(n.label_left, n.label_right, axis=0))
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, L.Concat(n.label_left, n.label_right, axis=0))
