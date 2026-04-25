
from sklearn.base import BaseEstimator
from sklearn.model_selection import GridSearchCV
import numpy as np

class CustomCV(BaseEstimator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.array([[i] for i in range(9)])  # 9 samples as features
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample targets

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Instantiate the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Example GridSearchCV
params = {'some_parameter': [0.1, 0.2]}
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
