
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split data into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = LogisticRegression(random_state=1)
clf3 = SVC(probability=True, random_state=1)

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('lr', clf2), 
    ('svc', clf3)],
    voting='soft'  # Use 'hard' for majority voting
)

# Here, you can fit on one of the datasets or a combined dataset
# For simplicity, we'll fit it on the first training set
voting_clf.fit(X1_train, y1_train)

# Make predictions on test sets
pred1 = voting_clf.predict(X1_test)
pred2 = voting_clf.predict(X2_test)
pred3 = voting_clf.predict(X3_test)

# Calculate accuracy for each model
accuracy1 = accuracy_score(y1_test, pred1)
accuracy2 = accuracy_score(y2_test, pred2)
accuracy3 = accuracy_score(y3_test, pred3)

print(f'Accuracy from model 1: {accuracy1:.2f}')
print(f'Accuracy from model 2: {accuracy2:.2f}')
print(f'Accuracy from model 3: {accuracy3:.2f}')

# Final ensemble prediction
final_predictions = voting_clf.predict(X1_test)  # You can use one of the test sets
