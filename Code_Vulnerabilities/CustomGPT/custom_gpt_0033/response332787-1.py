
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import GridSearchCV
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.arange(9).reshape(-1, 1)  # Example feature array with 9 samples
y = np.random.randint(0, 2, size=9)  # Random binary target

# Define custom indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate custom cross-validation
custom_cv = CustomCV(train_indices, test_indices)

# Define a parameter grid for GridSearchCV
param_grid = {'alpha': [0.1, 1, 10]}  # Example parameters for some model

# Create a GridSearchCV instance
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=param_grid, cv=custom_cv)

# Fit model
clf.fit(X, y)

# Best parameters
print("Best parameters found: ", clf.best_params_)
