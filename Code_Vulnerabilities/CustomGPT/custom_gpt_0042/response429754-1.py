
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# Load dataset (e.g., Iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# For binary classification, let's consider class 0 as positive and class 1 and 2 as negative
y_binary = np.where(y == 0, 1, 0)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.3, random_state=42)

# Train SVM classifier
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Predict the labels
y_pred = model.predict(X_test)

# Calculate confusion matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# Calculate FAR and FRR
FAR = fp / (fp + tn) if (fp + tn) > 0 else 0
FRR = fn / (fn + tp) if (fn + tp) > 0 else 0

# Output the results
print(f'False Acceptance Rate (FAR): {FAR:.2f}')
print(f'False Rejection Rate (FRR): {FRR:.2f}')
