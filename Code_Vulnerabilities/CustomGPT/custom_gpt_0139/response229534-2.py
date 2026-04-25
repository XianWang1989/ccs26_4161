
print("Max z:", np.nanmax(z), "Min z:", np.nanmin(z))  # Check for valid z-values
print("Any NaNs in z?", np.any(np.isnan(z)))  # Check for NaN values
print("Any Infs in z?", np.any(np.isinf(z)))  # Check for infinite values
