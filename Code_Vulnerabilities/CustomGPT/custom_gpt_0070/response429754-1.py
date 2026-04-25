
import numpy as np
from sklearn.metrics import confusion_matrix

# Example labels (ground truth) and predictions
y_true = np.array([1, 1, 0, 0, 1, 0, 1])  # 1 = Positive class, 0 = Negative class
y_pred = np.array([1, 0, 0, 1, 0, 0, 1])

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # Total negatives = fp + tn
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # Total positives = fn + tp

print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
