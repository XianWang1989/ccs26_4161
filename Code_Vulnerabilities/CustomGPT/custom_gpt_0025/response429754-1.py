
from sklearn.metrics import confusion_matrix

# Assume y_true are the true labels and y_pred are the predicted labels from SVM
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Example true labels
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]  # Example predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

# Output the results
print("False Acceptance Rate (FAR):", FAR)
print("False Rejection Rate (FRR):", FRR)
