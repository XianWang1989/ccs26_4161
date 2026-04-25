
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Generate example datasets (replace this with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define individual classifiers
classifier1 = DecisionTreeClassifier()
classifier2 = SVC(probability=True)  # Enable probability for SVC
classifier3 = LogisticRegression()

# Fit individual classifiers
classifier1.fit(X_train1, y_train1)
classifier2.fit(X_train2, y_train2)
classifier3.fit(X_train3, y_train3)

# Create a stacking classifier
estimators = [
    ('dt', classifier1),
    ('svc', classifier2),
    ('lr', classifier3)
]

stacking_classifier = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())

# Combine the predictions
# We can fit on a combined dataset for final predictions
X_combined_train = np.concatenate([X_train1, X_train2, X_train3])
y_combined_train = np.concatenate([y_train1, y_train2, y_train3])

stacking_classifier.fit(X_combined_train, y_combined_train)

# Test the stacking classifier
X_combined_test = np.concatenate([X_test1, X_test2, X_test3])
predictions = stacking_classifier.predict(X_combined_test)

# Print the predictions
print(predictions)
