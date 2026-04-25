
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample predicted labels and true labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0])  # True labels
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0])  # Predicted labels from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejection Rate
far = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate

print(f'False Rejection Rate (FRR): {frr:.2f}')
print(f'False Acceptance Rate (FAR): {far:.2f}')
