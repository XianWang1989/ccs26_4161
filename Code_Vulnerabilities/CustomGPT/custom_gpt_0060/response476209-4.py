
n.sig1 = L.Sigmoid(n.ip1, in_place=True)

# Forward
n.ip_f = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.loss_f = L.BinaryCrossEntropyLoss(n.ip_f, n.label_forward)

# Backward
n.ip_b = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.loss_b = L.BinaryCrossEntropyLoss(n.ip_b, n.label_backward)

# Left/Right
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.loss_lr = L.BinaryCrossEntropyLoss(n.ip_lr, n.label_lr)
