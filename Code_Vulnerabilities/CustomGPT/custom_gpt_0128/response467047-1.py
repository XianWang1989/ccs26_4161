
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Sample data (make sure to replace this with your actual data)
# Assuming X1, X2, X3 are your datasets and y is your labels.
X1, y = np.random.rand(100, 20), np.random.randint(0, 2, 100)  # Dataset 1
X2, y = np.random.rand(100, 20), np.random.randint(0, 2, 100)  # Dataset 2
X3, y = np.random.rand(100, 20), np.random.randint(0, 2, 100)  # Dataset 3

# Train-test split (you can also use your training data directly)
X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size=0.2, random_state=42)
X2_train, X2_test, _, _ = train_test_split(X2, y, test_size=0.2, random_state=42)
X3_train, X3_test, _, _ = train_test_split(X3, y, test_size=0.2, random_state=42)

# Initialize classifiers for each dataset
clf1 = DecisionTreeClassifier(random_state=42)
clf2 = SVC(probability=True, random_state=42)  # Probability=True for Voting
clf3 = LogisticRegression(random_state=42)

# Fit each classifier on its corresponding dataset
clf1.fit(X1_train, y_train)
clf2.fit(X2_train, y_train)
clf3.fit(X3_train, y_train)

# Create an ensemble of the classifiers
voting_clf = VotingClassifier(estimators=[('dt', clf1), ('svc', clf2), ('lr', clf3)], voting='soft')
voting_clf.fit(X1_train, y_train)

# Make predictions
predictions = voting_clf.predict(X1_test)  # Test on one of the datasets

# Evaluate predictions
accuracy = voting_clf.score(X1_test, y_test)
print(f'Ensemble Classifier Accuracy: {accuracy:.2f}')
