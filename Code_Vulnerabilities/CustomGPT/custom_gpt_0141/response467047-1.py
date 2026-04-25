
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample data generation for demonstration (replace this with your datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train-test split for the datasets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define classifiers
model1 = DecisionTreeClassifier(random_state=1)
model2 = SVC(probability=True, random_state=1)  # SVC needs probability=True for soft voting
model3 = LogisticRegression(random_state=1)

# Fit each model on its respective dataset
model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create a voting classifier
voting_classifier = VotingClassifier(
    estimators=[('dt', model1), ('svc', model2), ('lr', model3)],
    voting='soft'  # Use 'soft' for probability-based voting
)

# To combine predictions, fit the ensemble model on any of the datasets or a separate dataset
# For simplicity, let's assume we fit it on the first dataset:
voting_classifier.fit(X1_train, y1_train)

# Evaluate the ensemble on the test set (you can use any test set)
accuracy = voting_classifier.score(X1_test, y1_test)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
