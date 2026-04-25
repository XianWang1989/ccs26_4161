
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels
y_true = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]  # Actual labels
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]  # Predicted labels

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
frr = fn / (tp + fn) if (tp + fn) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
