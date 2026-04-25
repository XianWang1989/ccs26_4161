
# Adjusted Inner Product layer for the new combined label
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_left_right) # Update this reference
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right)
