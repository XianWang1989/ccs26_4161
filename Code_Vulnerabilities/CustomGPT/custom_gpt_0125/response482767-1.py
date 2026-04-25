
result = [
    (i, j, k) for i in [-4, -2, 1, 2, 5, 0]
                  for j in [-4, -2, 1, 2, 5, 0]
                  for k in [-4, -2, 1, 2, 5, 0] 
                  if i + j + k == 0
]
