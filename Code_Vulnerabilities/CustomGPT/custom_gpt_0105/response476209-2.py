
n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)
n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
n.sig1 = L.Sigmoid(n.ip1, in_place=True)

# Modify left and right to a single label
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))  # Two classes: Left or Right
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)  # Adjusted to label_lr
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

# Other labels remain unchanged
n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_f = L.Accuracy(n.ip_f, n.label_forward)
n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_b = L.Accuracy(n.ip_b, n.label_backward)
n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

n.ip_l = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_l = L.Accuracy(n.ip_l, n.label_left)
n.loss_l = L.SoftmaxWithLoss(n.ip_l, n.label_left)
