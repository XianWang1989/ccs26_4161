
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# Sample data (replace with your actual data)
true_labels = np.array([1, 0, 1, 1, 0, 0, 1])  # True labels
predicted_labels = np.array([1, 1, 0, 1, 0, 0, 0])  # Predicted labels

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Acceptance Rate
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Rejection Rate

# Output the results
print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
