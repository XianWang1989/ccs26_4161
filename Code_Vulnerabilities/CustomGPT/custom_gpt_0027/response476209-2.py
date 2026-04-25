
# Combined left-right
n.ip_lr = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)  # Assuming label_lr is defined
