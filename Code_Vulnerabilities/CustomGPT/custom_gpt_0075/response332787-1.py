
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

# Generate sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your custom train-test indices
train_indices = [1, 3, 5, 7, 8]  # Train for the 1st fold
test_indices = [0, 2, 4, 6]       # Test for the 1st fold

# Create the split identifiers
# -1 for the test samples, 0 for the train samples
splitter = PredefinedSplit(test_fold=[-1 if i in train_indices else 0 for i in range(len(y))])

# Set parameters for GridSearchCV
params = {'max_depth': [1, 2, 3, 4, 5]}
clf = GridSearchCV(DecisionTreeClassifier(), params, cv=splitter)

# Fit the model
clf.fit(X, y)

# Output best parameters
print("Best parameters:", clf.best_params_)
