
import numpy as np
from sklearn.model_selection import GridSearchCV, check_cv
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Define custom cross-validation generator
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Parameters for GridSearchCV
param_grid = {'n_estimators': [10, 50], 'max_depth': [None, 10, 20]}
clf = GridSearchCV(RandomForestClassifier(), param_grid, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output results
print(f"Best parameters: {clf.best_params_}")
