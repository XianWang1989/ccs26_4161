
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Custom cross-validation class
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

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]  # Note indices should be zero-based
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate your custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'n_estimators': [10, 20], 'max_depth': [None, 10]}

# Initialize GridSearchCV with the custom CV
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Best parameters
print("Best parameters found: ", clf.best_params_)
