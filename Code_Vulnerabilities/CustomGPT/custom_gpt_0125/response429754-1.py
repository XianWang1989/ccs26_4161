
import numpy as np
from sklearn.metrics import confusion_matrix

# Assuming y_true are the true labels and y_pred are the predicted labels
y_true = np.array([0, 0, 1, 1, 0, 1, 1, 0])  # Actual labels
y_pred = np.array([0, 1, 1, 0, 0, 1, 0, 0])  # Predicted labels

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) != 0 else 0  # False Acceptance Rate
FRR = fn / (fn + tp) if (fn + tp) != 0 else 0  # False Rejection Rate

print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
