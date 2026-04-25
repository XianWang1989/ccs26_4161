
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = [1, 0, 1, 1, 0, 0, 1, 0]
predicted_labels = [1, 0, 0, 1, 0, 1, 1, 0]

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (tp + fn) if (tp + fn) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
