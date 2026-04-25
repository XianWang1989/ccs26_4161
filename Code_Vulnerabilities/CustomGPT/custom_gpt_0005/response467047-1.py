
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate synthetic data for illustration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into train and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.3, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Define classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2) # Set probability=True for VotingClassifier
clf3 = LogisticRegression(random_state=3)

# Train classifiers
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)
], voting='soft')  # Use 'soft' for probability-based votes

# Train the voting classifier on a combination of datasets
combined_X_train = np.concatenate((X_train1, X_train2, X_train3))
combined_y_train = np.concatenate((y_train1, y_train2, y_train3))
voting_clf.fit(combined_X_train, combined_y_train)

# Make predictions
combined_X_test = np.concatenate((X_test1, X_test2, X_test3))
combined_y_test = np.concatenate((y_test1, y_test2, y_test3))
y_pred = voting_clf.predict(combined_X_test)

# Evaluate the ensemble model
accuracy = accuracy_score(combined_y_test, y_pred)
print(f'Ensemble model accuracy: {accuracy:.2f}')
