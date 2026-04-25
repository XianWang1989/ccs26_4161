
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels from SVM
y_true = [0, 1, 1, 0, 0, 1, 0, 1]  # Actual labels
y_pred = [0, 1, 0, 0, 1, 1, 0, 0]  # Predicted labels

# Create confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
