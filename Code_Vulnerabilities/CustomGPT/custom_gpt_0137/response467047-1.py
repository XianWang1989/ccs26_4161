
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Create synthetic datasets for demonstration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers
clf1 = DecisionTreeClassifier()
clf2 = SVC(probability=True)  # Set probability=True for soft voting
clf3 = RandomForestClassifier()

# Train classifiers on their respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Ensemble classifier using VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('tree', clf1),
    ('svc', clf2),
    ('rf', clf3)
], voting='soft')  # Use 'soft' for averaging probabilities

# Fit the ensemble model on one of the datasets (or a combined set)
voting_clf.fit(X_train1, y_train1)  # You can choose any dataset for fitting

# Make predictions on a test set (you may choose to test on any of the datasets)
predictions = voting_clf.predict(X_test1)

# Output the predictions
print("Ensemble Predictions:", predictions)

# Evaluate the model accuracy if necessary
accuracy = voting_clf.score(X_test1, y_test1)  # Replace with the appropriate test set
print("Accuracy:", accuracy)
