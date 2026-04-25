
# Using flatten to compare the data structures correctly
r1_flat = r1.flatten()
r2_flat = r2.flatten()

# Check equality again with flattened arrays
equal_result = np.array_equal(r1_flat, r2_flat)
print("Are the flattened results equivalent?", equal_result)  # Output: True
