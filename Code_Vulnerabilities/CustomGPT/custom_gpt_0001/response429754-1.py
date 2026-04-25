
from sklearn.metrics import confusion_matrix

# Example: True labels and predicted labels from your SVM classifier
# Here, 1 represents positive class, and 0 represents negative class
true_labels = [1, 0, 1, 1, 0, 0, 0, 1]  # example true labels
predicted_labels = [1, 0, 0, 1, 0, 1, 0, 1]  # example predicted labels

# Calculate confusion matrix
TN, FP, FN, TP = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0  # Avoid division by zero
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
