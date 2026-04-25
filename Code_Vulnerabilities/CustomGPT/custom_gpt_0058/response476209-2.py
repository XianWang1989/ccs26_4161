
# Replace these lines:
n.ip_r = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_r = L.Accuracy(n.ip_r, n.label_right)
n.loss_r = L.SoftmaxWithLoss(n.ip_r, n.label_right)

# With this combined layer:
n.ip_side = L.InnerProduct(n.sig1, num_output=2, weight_filler=dict(type='xavier'))
n.accuracy_side = L.Accuracy(n.ip_side, n.label_side)
n.loss_side = L.SoftmaxWithLoss(n.ip_side, n.label_side)
