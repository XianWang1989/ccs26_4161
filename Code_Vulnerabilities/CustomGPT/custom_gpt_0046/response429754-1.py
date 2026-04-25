
import numpy as np
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Sample data
X = np.array([[feature_vector1], [feature_vector2], ...])  # Replace with your dataset
y = np.array([0, 1, 0, 1, ...])  # Replace with your labels (0 for negative, 1 for positive)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM classifier
model = SVC(kernel='linear')  # You can choose any kernel
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Calculating FAR and FRR
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)

TN, FP, FN, TP = confusion_matrix.ravel()

FAR = FP / (FP + TN) if (FP + TN) > 0 else 0  # False Acceptance Rate
FRR = FN / (TP + FN) if (TP + FN) > 0 else 0  # False Rejection Rate

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
