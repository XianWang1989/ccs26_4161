
n.join_speed = L.Concat(n.relu4, n.data_speed, in_place=True)

# Combining left and right outputs into a single label
n.label_lr = L.Input(shape=dict(dim=[N, 1]))  # Change your dataset accordingly

# Inner product layer after concatenation
n.ip1 = L.InnerProduct(n.join_speed, num_output=512, weight_filler=dict(type='xavier'))
n.relu5 = L.ReLU(n.ip1, in_place=True)  # Adding an activation function after IP layer

# Outputs for Forward and Backward
n.ip_f = L.InnerProduct(n.relu5, num_output=2, weight_filler=dict(type='xavier'))
n.loss_f = L.SoftmaxWithLoss(n.ip_f, n.label_forward)

n.ip_b = L.InnerProduct(n.relu5, num_output=2, weight_filler=dict(type='xavier'))
n.loss_b = L.SoftmaxWithLoss(n.ip_b, n.label_backward)

# Combined Left/Right output
n.ip_lr = L.InnerProduct(n.relu5, num_output=2, weight_filler=dict(type='xavier'))
n.loss_lr = L.SoftmaxWithLoss(n.ip_lr, n.label_lr)
