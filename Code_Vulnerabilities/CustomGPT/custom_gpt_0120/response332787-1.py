
import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_index, test_index in zip(self.train_indices, self.test_indices):
            yield train_index, test_index

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Initialize custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Set up GridSearchCV
params = {'C': [0.1, 1, 10]}
clf = GridSearchCV(LogisticRegression(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Display results
print("Best parameters found:", clf.best_params_)
