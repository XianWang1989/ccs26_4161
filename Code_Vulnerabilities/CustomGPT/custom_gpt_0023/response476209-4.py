
n.ip_all = L.InnerProduct(n.sig1, num_output=4, weight_filler=dict(type='xavier'))
n.softmax_all = L.Softmax(n.ip_all)
n.loss_all = L.SoftmaxWithLoss(n.ip_all, n.label_combined)  # Combined labels
