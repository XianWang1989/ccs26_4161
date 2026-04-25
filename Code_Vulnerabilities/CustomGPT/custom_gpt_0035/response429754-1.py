
from sklearn.metrics import confusion_matrix

# Assuming y_true are the true labels and y_pred are the predicted labels from SVM
y_true = [1, 0, 1, 1, 0, 0, 1]  # Example ground truth values
y_pred = [1, 0, 0, 1, 0, 1, 1]  # Example predictions

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Total negatives = tn + fp
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Total positives = fn + tp

print(f"False Acceptance Rate (FAR): {FAR:.4f}")
print(f"False Rejection Rate (FRR): {FRR:.4f}")
