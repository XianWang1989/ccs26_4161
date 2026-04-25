
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create synthetic datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)  # probability=True for soft voting
clf3 = LogisticRegression(random_state=3)

clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create an ensemble model using VotingClassifier
voting_clf = VotingClassifier(
    estimators=[('rf', clf1), ('svc', clf2), ('lr', clf3)],
    voting='soft'  # Use 'hard' for majority voting
)

# Fit the ensemble model on any of the datasets (assuming they have similar labels)
voting_clf.fit(X_train1, y_train1)  # You can choose any dataset

# Evaluate the ensemble model
accuracy = voting_clf.score(X_test1, y_test1)  # Test on the same dataset
print(f"Accuracy of voting classifier: {accuracy:.2f}")
