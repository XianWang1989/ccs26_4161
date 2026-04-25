
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into train and test sets
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers for each dataset
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()
clf3 = RandomForestClassifier()

# Train the classifiers
clf1.fit(X_train_1, y_train_1)
clf2.fit(X_train_2, y_train_2)
clf3.fit(X_train_3, y_train_3)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('logreg', clf1), 
    ('dt', clf2), 
    ('rf', clf3)],
    voting='hard'  # Use 'soft' for probability-based voting
)

# Fit the voting classifier on the same training data (you may combine features as needed)
voting_clf.fit(X_train_1, y_train_1)  # For this example, you can use any of the datasets

# Evaluate on test dataset (Choose any test set)
accuracy = voting_clf.score(X_test_1, y_test_1)
print(f'Voting Classifier accuracy: {accuracy:.2f}')
