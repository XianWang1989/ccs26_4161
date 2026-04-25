
import numpy as np
from sklearn.metrics import confusion_matrix

# Assuming y_true is your true labels and y_pred is your predicted labels
y_true = np.array([1, 1, 0, 1, 0, 0, 1, 0])  # Replace with your actual true labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 0, 0])  # Replace with your SVM predicted labels

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
