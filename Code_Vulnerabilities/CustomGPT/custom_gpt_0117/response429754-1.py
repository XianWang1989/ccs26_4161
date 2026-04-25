
import numpy as np

# True labels and predicted labels
y_true = np.array([1, 1, 0, 0, 1, 0])  # 1 = match, 0 = non-match
y_pred = np.array([1, 0, 0, 1, 1, 0])  # SVM predictions

# Calculate False Accepts (F) and False Rejects (R)
false_accepts = np.sum((y_true == 0) & (y_pred == 1))  # Non-matches accepted as matches
false_rejects = np.sum((y_true == 1) & (y_pred == 0))  # Matches rejected as non-matches

# Calculate totals
total_non_matches = np.sum(y_true == 0)
total_matches = np.sum(y_true == 1)

# Calculate FAR and FRR
FAR = false_accepts / total_non_matches if total_non_matches > 0 else 0
FRR = false_rejects / total_matches if total_matches > 0 else 0

# Output results
print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
