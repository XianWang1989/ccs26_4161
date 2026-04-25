
n.join_speed = L.Concat(n.relu4, n.data_speed, axis=1)
n.fc1 = L.InnerProduct(n.join_speed, num_output=3, weight_filler=dict(type='xavier'))
