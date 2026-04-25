
from sklearn.metrics import confusion_matrix

# Example data: true labels and predicted labels
y_true = [1, 0, 1, 1, 0, 0, 1, 0]  # Actual labels (1: positive, 0: negative)
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Total Actual Negatives = tn + fp
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Total Actual Positives = fn + tp

# Print results
print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
