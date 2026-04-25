
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels from SVM
true_labels = np.array([1, 0, 1, 1, 0, 0, 1, 0])  # Example true labels
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 1, 0])  # Example predicted labels from SVM

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR (False Acceptance Rate)
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0

# Calculate FRR (False Rejection Rate)
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

# Results
print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
