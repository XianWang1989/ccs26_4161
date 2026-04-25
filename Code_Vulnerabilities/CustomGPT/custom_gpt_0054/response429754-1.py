
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Load dataset (e.g., Iris dataset) for simplicity
iris = datasets.load_iris()
X = iris.data
y = iris.target

# For binary classification, we'll only consider two classes
X = X[y != 2]  # Keeping only two classes
y = y[y != 2]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Generate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"False Acceptance Rate (FAR): {FAR:.2f}")
print(f"False Rejection Rate (FRR): {FRR:.2f}")
