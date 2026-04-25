
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
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

# Generate sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom train-test indices
train_indices = [[0, 1, 3, 4, 5, 6, 7, 8], [0, 2, 3, 4, 5, 6, 7, 8]]
test_indices = [[2, 8], [1]]

custom_cv = CustomCV(train_indices, test_indices)

# Example parameter grid for a classifier, e.g., RandomForest
params = {'n_estimators': [10, 50], 'max_depth': [None, 10]}

# Use GridSearchCV with the custom cross-validation
clf = GridSearchCV(estimator=BaseEstimator(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Best parameters found
print(clf.best_params_)
