
lx = [3.625, 4.625]
ly = [41.435, 42.435]
xy = list(itertools.product(lx, ly))  # xy = [(3.625, 41.435), (3.625, 42.435), ...]

b = -1
for l in xy:
    b += 1
    # Error occurs here:
    print(l[b])  # l[b] is a float here, this will raise error
