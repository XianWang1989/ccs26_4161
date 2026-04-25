
n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)

# Modified output layer for combined left/right labels
n.ip_lr = L.InnerProduct(n.join_speed, num_output=3, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

# Keep your existing structure for forward and backward labels
n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_f = L.Accuracy(n.ip_f, n.label_forward)
n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_b = L.Accuracy(n.ip_b, n.label_backward)
n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)
