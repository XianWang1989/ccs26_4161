
import numpy as np
from sklearn.metrics import confusion_matrix

# Sample true labels and predicted labels from SVM
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])  # 1 = positive, 0 = negative
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])  # SVM predictions

# Calculate the confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Calculate FAR and FRR
far = fp / (fp + tn) if (fp + tn) > 0 else 0  # FAR = FP / (FP + TN)
frr = fn / (fn + tp) if (fn + tp) > 0 else 0  # FRR = FN / (FN + TP)

print(f"False Acceptance Rate (FAR): {far:.2f}")
print(f"False Rejection Rate (FRR): {frr:.2f}")
