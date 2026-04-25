
n.label_direction = n[label_direction]

n.ip_dir = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))
n.accuracy_dir = L.Accuracy(n.ip_dir, n.label_direction)
n.loss_dir = L.SoftmaxWithLoss(n.ip_dir, n.label_direction)
