
# Modified for left/right arrow conflict resolution
data_left_right = L.InnerProduct(n.sig1, num_output=3, weight_filler=dict(type='xavier'))
n.accuracy_lr = L.Accuracy(data_left_right, n.label_left_right)  # Create a left_right label where 0 = left, 1 = right, 2 = none
n.loss_lr = L.SoftmaxWithLoss(data_left_right, n.label_left_right)
