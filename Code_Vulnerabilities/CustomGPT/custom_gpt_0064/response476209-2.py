
n.label_lr = L.Input(n.label_forward, num_output=3)  # Assuming 3 classes: forward, backward, left/right

# Modify the output for the left/right combined label
n.ip_lr = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
n.accuracy_lr = L.Accuracy(n.ip_lr, n.label_lr)
