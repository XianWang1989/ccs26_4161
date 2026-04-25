
# Combine left and right labels into one output
n.label_lr = L.Input(n.label_left, n.label_right)
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)

# Other outputs remain unchanged
# ...
