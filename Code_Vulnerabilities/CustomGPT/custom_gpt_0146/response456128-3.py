
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product of each row of X with every other row of X
# This will give us a list of outer products
outer_products = [np.outer(row.A.flatten(), row.A.flatten()) for row in X]

# Concatenate the result into a single array
r1 = np.concatenate(outer_products, axis=0)

# Now calculate r2 as the sum of outer products (or another equivalent method)
# But note that r2 resulting from dot(X, X.T) will generally differ in dimension and shape.
r2 = None  # Here you'd have to decide the exact equivalency for your need.

# Comparison - as they represent different mathematical concepts, cannot truly substitute directly
# Using the actual row-wise outer products as r1

# To visualize that it produces outer products, print the output
for i, outer_product in enumerate(outer_products):
    print(f"Outer product for row {i}:")
    print(outer_product)

# Since r1 and r2 are not directly comparable, we adjust our expectations based on output types.
