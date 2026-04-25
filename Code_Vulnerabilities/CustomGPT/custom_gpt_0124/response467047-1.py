
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Generate sample datasets (replace this with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split datasets into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
clf1 = RandomForestClassifier(random_state=1)
clf1.fit(X_train1, y_train1)

clf2 = LogisticRegression(random_state=2)
clf2.fit(X_train2, y_train2)

clf3 = SVC(probability=True, random_state=3)
clf3.fit(X_train3, y_train3)

# Create a VotingClassifier
voting_clf = VotingClassifier(
    estimators=[('rf', clf1), ('lr', clf2), ('svc', clf3)],
    voting='soft'  # Use 'soft' to use predicted probabilities
)

# Fit the ensemble model on one of the datasets (or their combined features)
# For simplicity, we'll use the first dataset's samples
voting_clf.fit(X_train1, y_train1)

# Make predictions
predictions = voting_clf.predict(X_test1)

# Evaluate the performance
accuracy = voting_clf.score(X_test1, y_test1)
print(f'Ensemble model accuracy: {accuracy:.2f}')
