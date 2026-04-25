
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate synthetic datasets (as an example)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and testing
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.3, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.3, random_state=42)

# Create individual classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = LogisticRegression(random_state=1)
clf3 = SVC(probability=True, random_state=1)

# Fit each classifier to its corresponding dataset
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Now create a Voting Classifier using the trained classifiers
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('lr', clf2), 
    ('svc', clf3)
], voting='hard')  # You can use 'soft' for probability-based voting if appropriate

# Combine datasets for final training
X_combined = np.vstack((X_train1, X_train2, X_train3))
y_combined = np.concatenate((y_train1, y_train2, y_train3))

# Fit the voting classifier to the combined dataset
voting_clf.fit(X_combined, y_combined)

# Make predictions on the test set (using one of the datasets for testing)
y_pred = voting_clf.predict(X_test1)  # Change this line as needed for other datasets

# Evaluate the ensemble model
accuracy = accuracy_score(y_test1, y_pred)
print(f'Accuracy of the ensemble model: {accuracy:.2f}')
