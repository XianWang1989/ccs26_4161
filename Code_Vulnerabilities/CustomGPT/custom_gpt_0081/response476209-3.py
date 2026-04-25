
n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # 0: none, 1: left, 2: right
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_left_right)
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_left_right)
