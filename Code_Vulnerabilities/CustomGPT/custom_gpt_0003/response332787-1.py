
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
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

# Sample dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Defined indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of CustomCV
custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for GridSearchCV
params = {'max_depth': [1, 2, 3]}

# Implement GridSearchCV using the custom cross-validation strategy
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Output best parameters
print("Best parameters found:", clf.best_params_)
