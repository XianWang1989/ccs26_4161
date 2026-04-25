
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define classifiers
classifier1 = LogisticRegression()
classifier2 = RandomForestClassifier()
classifier3 = SVC(probability=True)

# Fit classifiers on each dataset
classifier1.fit(X1_train, y1_train)
classifier2.fit(X2_train, y2_train)
classifier3.fit(X3_train, y3_train)

# Use the classifiers to predict on the test sets
pred1 = classifier1.predict(X1_test)
pred2 = classifier2.predict(X2_test)
pred3 = classifier3.predict(X3_test)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('lr', classifier1), ('rf', classifier2), ('svc', classifier3)],
    voting='soft')  # Use 'soft' so that predicted probabilities are used

# Train the Voting Classifier on the first dataset
voting_clf.fit(X1_train, y1_train)

# Make predictions using the voting classifier
final_pred = voting_clf.predict(X1_test)

# Evaluate the performance
accuracy = accuracy_score(y1_test, final_pred)
print(f'Ensemble Accuracy: {accuracy:.2f}')

# Note: Depending on the context, you can fit on different datasets respectively.
