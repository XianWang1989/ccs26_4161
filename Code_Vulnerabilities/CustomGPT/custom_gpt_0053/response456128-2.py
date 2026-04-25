
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product of each row with itself
outer_products = np.array([np.outer(X[i], X[i]) for i in range(X.shape[0])])

# Now calculate dot products
dot_product = np.dot(X, X.T)

# Print results to compare
print("Outer Products:")
print(outer_products)

print("\nDot Product:")
print(dot_product)

# Checking array equality for outer products with the combined shape
# Here we check for each outer product row
for i in range(outer_products.shape[0]):
    print(f"Array equal for row {i}: {np.array_equal(outer_products[i], dot_product)}")
