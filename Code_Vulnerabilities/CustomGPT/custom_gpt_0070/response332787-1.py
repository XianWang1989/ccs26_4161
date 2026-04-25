
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Custom Cross-Validator
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

# Sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Instantiate custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Set up GridSearchCV
params = {'n_estimators': [10, 20], 'max_depth': [None, 5, 10]}
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit model
clf.fit(X, y)

# Best parameters
print("Best parameters found: ", clf.best_params_)
