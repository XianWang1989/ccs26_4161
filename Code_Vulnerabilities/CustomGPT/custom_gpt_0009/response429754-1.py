
from sklearn.metrics import confusion_matrix

# Sample true labels and predictions from your SVM classifier
y_true = [1, 0, 1, 1, 0, 1, 0, 0]  # Actual labels (1 for positive, 0 for negative)
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]  # Predicted labels by SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn)  # False Acceptance Rate
FRR = fn / (fn + tp)  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
