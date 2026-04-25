
from sklearn import metrics
import numpy as np

# Example ground truth (actual labels)
y_true = np.array([1, 1, 1, 0, 0, 1, 0, 0, 0, 1])  # 1 = positive, 0 = negative

# Example predicted labels from your SVM model
y_pred = np.array([1, 0, 1, 0, 1, 0, 0, 0, 1, 1])  # Hypothetical predictions

# Calculate confusion matrix
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
fnr = fn / (tp + fn) if (tp + fn) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {fnr:.2f}")
