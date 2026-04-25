
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate synthetic data for demonstration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split data into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define the classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)
clf3 = LogisticRegression(random_state=3)

# Train each model on its respective dataset
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create an ensemble of the classifiers
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('svc', clf2), 
    ('lr', clf3)],
    voting='soft'  # Use 'soft' for probability-based voting
)

# Fit the ensemble on one of the datasets
voting_clf.fit(X_train1, y_train1)  # You can choose any dataset for this

# Evaluate on a test set (you can mix test sets or take one)
accuracy = voting_clf.score(X_test1, y_test1)  # Change as needed
print(f'Ensemble Accuracy on Test Set: {accuracy:.2f}')
