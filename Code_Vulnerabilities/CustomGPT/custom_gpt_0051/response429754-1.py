
import numpy as np
from sklearn.metrics import confusion_matrix

# Example ground truth labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0])  # 1 for positive class, 0 for negative class
y_pred = np.array([1, 0, 0, 1, 0, 0, 1])  # SVM predicted class labels

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
