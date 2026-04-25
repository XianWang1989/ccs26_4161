
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from sklearn.model_selection import BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np

# Create a custom cross-validation iterator
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your own set of train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Initialize our custom CV
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define parameters for GridSearchCV
params = {'C': [0.1, 1, 10]}

# Initialize GridSearchCV with the custom CV
clf = GridSearchCV(LogisticRegression(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Print the best parameters
print("Best parameters found: ", clf.best_params_)
