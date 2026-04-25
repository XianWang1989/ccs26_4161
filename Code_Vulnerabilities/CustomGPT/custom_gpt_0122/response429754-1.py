
from sklearn.metrics import confusion_matrix

# Example data
true_labels = [1, 0, 1, 1, 0, 0, 1]  # True labels: 1 = positive, 0 = negative
predicted_labels = [1, 0, 0, 1, 1, 0, 1]  # Predicted labels from SVM

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
total_negatives = tn + fp
total_positives = tp + fn

fpr = fp / total_negatives if total_negatives > 0 else 0  # False Acceptance Rate
frr = fn / total_positives if total_positives > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
