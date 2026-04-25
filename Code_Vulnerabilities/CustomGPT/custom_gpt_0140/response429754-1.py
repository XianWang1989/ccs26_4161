
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

# Sample data
# Assuming you have features X and labels y.
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # 0: negative, 1: positive

# Train SVM Classifier
model = svm.SVC()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Compute confusion matrix
TN, FP, FN, TP = confusion_matrix(y, predictions).ravel()

# Calculate FAR and FRR
FAR = FP / (FP + TN) if (FP + TN) > 0 else 0
FRR = FN / (FN + TP) if (FN + TP) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
