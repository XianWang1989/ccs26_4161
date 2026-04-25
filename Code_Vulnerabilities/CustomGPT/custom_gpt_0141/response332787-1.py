
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import make_classification
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Create some sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your custom train-test splits
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of the custom cross-validation class
custom_cv = CustomCV(train_indices, test_indices)

# Example parameter grid for a classifier (e.g., Logistic Regression)
from sklearn.linear_model import LogisticRegression

param_grid = {'C': [0.1, 1, 10]}
clf = GridSearchCV(LogisticRegression(), param_grid, cv=custom_cv)

# Fit the model using the GridSearchCV
clf.fit(X, y)

# Display the best parameters found
print("Best parameters found: ", clf.best_params_)
