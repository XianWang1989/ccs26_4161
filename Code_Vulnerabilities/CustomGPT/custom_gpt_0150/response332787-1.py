
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate your custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Set up GridSearchCV
param_grid = {'n_estimators': [10, 50, 100]}
clf = GridSearchCV(RandomForestClassifier(), param_grid, cv=custom_cv)

# Fit model
clf.fit(X, y)

# Print best parameters
print("Best parameters found: ", clf.best_params_)
