
from sklearn.metrics import confusion_matrix

# Assuming y_true is the actual labels and y_pred is the predicted labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Example actual labels (1 for positive class, 0 for negative class)
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]  # Example predicted labels from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
