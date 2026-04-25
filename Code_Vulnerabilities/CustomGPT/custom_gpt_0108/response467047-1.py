
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.3, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.3, random_state=42)

# Train classifiers on each dataset
clf1 = DecisionTreeClassifier()
clf2 = RandomForestClassifier()
clf3 = LogisticRegression()

clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create Voting Ensemble
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1),
    ('rf', clf2),
    ('lr', clf3)
], voting='hard')  # Use 'soft' for probability voting

# Fit the voting classifier on combined dataset (or test set if available)
X_combined = np.vstack((X_test1, X_test2, X_test3))
y_combined = np.hstack((y_test1, y_test2, y_test3))

voting_clf.fit(X_combined, y_combined)
voting_predictions = voting_clf.predict(X_combined)

# Create Stacking Ensemble
stacking_clf = StackingClassifier(estimators=[
    ('dt', clf1),
    ('rf', clf2),
    ('lr', clf3)
], final_estimator=LogisticRegression())

stacking_clf.fit(X_combined, y_combined)
stacking_predictions = stacking_clf.predict(X_combined)

print("Voting Predictions:", voting_predictions)
print("Stacking Predictions:", stacking_predictions)
