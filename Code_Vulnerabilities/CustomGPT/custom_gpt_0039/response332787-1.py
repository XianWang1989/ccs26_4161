
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, is_classifier
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

# Example data
X = np.random.rand(9, 3)  # 9 samples, 3 features
y = np.random.randint(0, 2, size=9)  # Binary targets

# Custom indices for 2-fold CV
train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

# Create an instance of CustomCV
custom_cv = CustomCV(train_indices, test_indices)

# Use GridSearchCV with the custom cross-validation
params = {'param1': [0.1, 0.2], 'param2': [1, 2]}  # Example parameters
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
