
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Generate sample datasets (replace with your own datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define classifiers for each dataset
classifier1 = LogisticRegression()
classifier2 = DecisionTreeClassifier()
classifier3 = SVC(probability=True)  # SVC requires probability=True for VotingClassifier

# Train classifiers on their respective datasets
classifier1.fit(X_train1, y_train1)
classifier2.fit(X_train2, y_train2)
classifier3.fit(X_train3, y_train3)

# Create a VotingClassifier for hard or soft voting
voting_classifier = VotingClassifier(estimators=[
    ('lr', classifier1),
    ('dt', classifier2),
    ('svc', classifier3)
], voting='soft')  # use 'hard' for majority voting

# Train the ensemble model (optional: you can also use it directly without additional training)
# Here, we train on average to represent the datasets
X_all_train = np.vstack((X_train1, X_train2, X_train3))
y_all_train = np.concatenate((y_train1, y_train2, y_train3))

voting_classifier.fit(X_all_train, y_all_train)

# Evaluate on a test set (You can combine the test sets as well)
X_test_all = np.vstack((X_test1, X_test2, X_test3))
y_test_all = np.concatenate((y_test1, y_test2, y_test3))

# Make predictions
predictions = voting_classifier.predict(X_test_all)

# Print results
print("Predictions:", predictions)
