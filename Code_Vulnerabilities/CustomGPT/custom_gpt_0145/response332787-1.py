
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
import numpy as np

# Sample dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Initialize custom cross-validation
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define parameters for GridSearchCV
params = {'param1': [0, 1], 'param2': [10, 20]}

# Implement GridSearchCV with the custom cross-validation
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
