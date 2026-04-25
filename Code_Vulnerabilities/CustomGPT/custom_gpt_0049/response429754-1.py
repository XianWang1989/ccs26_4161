
from sklearn.metrics import confusion_matrix

# Assuming you have the true labels and predicted labels from your SVM
# true_labels = [1, 0, 1, 1, 0, 1]
# predicted_labels = [1, 0, 0, 1, 0, 1]

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
total_negatives = tn + fp  # True Negatives + False Positives
total_positives = tp + fn   # True Positives + False Negatives

FAR = fp / total_negatives if total_negatives > 0 else 0
FRR = fn / total_positives if total_positives > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
