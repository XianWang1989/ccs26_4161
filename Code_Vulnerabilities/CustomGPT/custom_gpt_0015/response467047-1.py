
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Initialize classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)  # probability=True to enable soft voting
clf3 = LogisticRegression(random_state=3)

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Combine classifiers using VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)],
    voting='soft'  # Use 'hard' for majority voting
)

# Fit the voting classifier on one of the datasets (e.g., X1)
voting_clf.fit(X1_train, y1_train)

# Make predictions on test sets
preds1 = voting_clf.predict(X1_test)
preds2 = voting_clf.predict(X2_test)
preds3 = voting_clf.predict(X3_test)

# Display predictions
print("Predictions for dataset 1:", preds1)
print("Predictions for dataset 2:", preds2)
print("Predictions for dataset 3:", preds3)
