
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = [0, 1, 1, 0, 1, 0]  # 0 = negative, 1 = positive
predicted_labels = [0, 1, 0, 0, 1, 1]  # Predictions from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Handle division by zero
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Handle division by zero

print(f"False Acceptance Rate (FAR): {FAR}")
print(f"False Rejection Rate (FRR): {FRR}")
