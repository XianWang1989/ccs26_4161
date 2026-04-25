
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.model_selection import BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def _iter_test_indices(self):
        for test_idx in self.test_indices:
            yield test_idx

# Example data
X = np.arange(9).reshape((9, 1))  # 9 samples
y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 0])  # Sample targets

# Custom indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Parameters for the GridSearch
params = {'model__parameter': [0.1, 0.2, 0.3]}  # example parameter

# Create a GridSearchCV instance
clf = GridSearchCV(estimator=<your_model>, param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
