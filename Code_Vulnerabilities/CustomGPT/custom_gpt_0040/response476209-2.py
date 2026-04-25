
n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))  # 0 = None, 1 = Left, 2 = Right
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.labels)  # single softmax loss for left/right
