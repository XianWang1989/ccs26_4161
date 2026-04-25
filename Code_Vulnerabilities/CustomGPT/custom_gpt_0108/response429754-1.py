
import numpy as np
from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
true_labels = np.array([1, 1, 0, 1, 0, 0, 1, 0])  # 1: Positive, 0: Negative
predicted_labels = np.array([1, 0, 0, 1, 0, 1, 0, 0])  # SVM predictions

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(true_labels, predicted_labels).ravel()

# Calculate FAR and FRR
fpr = fp / (fp + tn)  # False Positive Rate = FAR
frr = fn / (fn + tp)  # False Negative Rate = FRR

print(f"False Acceptance Rate (FAR): {fpr:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
