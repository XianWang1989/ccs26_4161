
from sklearn.metrics import confusion_matrix

# Sample true and predicted labels
y_true = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]  # Actual classes
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]  # Predicted classes

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
