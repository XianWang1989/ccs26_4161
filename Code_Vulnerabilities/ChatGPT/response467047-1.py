
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic data for three different datasets
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split data into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=0)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=0)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=0)

# Create three different classifiers
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()
clf3 = SVC(probability=True)  # Use probability=True for soft voting

# Train each classifier on its respective dataset
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
votes = VotingClassifier(estimators=[
    ('lr', clf1), 
    ('dt', clf2), 
    ('svc', clf3)],
    voting='soft'  # Use 'hard' for majority voting or 'soft' for probabilistic voting
)

# Make a combined training set from the outputs of the individual classifiers
X_combined_train = np.column_stack((
    clf1.predict_proba(X1_test)[:, 1],   # Select probability of class 1
    clf2.predict_proba(X2_test)[:, 1],
    clf3.predict_proba(X3_test)[:, 1]
))

# Fit the VotingClassifier on the combined training set
votes.fit(X_combined_train, y1_test)  # Using any set of labels is okay, you just need consistent labels

# Make predictions
X_combined_test = np.column_stack((
    clf1.predict_proba(X1_test)[:, 1],
    clf2.predict_proba(X2_test)[:, 1],
    clf3.predict_proba(X3_test)[:, 1]
))

# Get predictions from the voting classifier
y_pred = votes.predict(X_combined_test)

# Evaluate the performance
accuracy = accuracy_score(y1_test, y_pred)  # Change 'y1_test' to the appropriate test labels
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
