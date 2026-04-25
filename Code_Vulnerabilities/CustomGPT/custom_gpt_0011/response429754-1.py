
from sklearn.metrics import confusion_matrix

# Assuming y_true is the true labels and y_pred is the predictions from your SVM model
y_true = [1, 0, 1, 0, 1, 0, 0, 1]  # Example true labels
y_pred = [1, 0, 0, 0, 1, 1, 0, 1]  # Example predicted labels

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) != 0 else 0  # Avoid division by zero
FRR = fn / (fn + tp) if (fn + tp) != 0 else 0  # Avoid division by zero

print(f"False Acceptance Rate (FAR): {FAR}")
print(f"False Rejection Rate (FRR): {FRR}")
