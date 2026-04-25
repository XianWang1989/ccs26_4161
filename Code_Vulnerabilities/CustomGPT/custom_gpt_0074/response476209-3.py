
n.ip_direction = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))
n.accuracy_direction = L.Accuracy(n.ip_direction, n.label_direction)
n.loss_direction = L.SoftmaxWithLoss(n.ip_direction, n.label_direction)
