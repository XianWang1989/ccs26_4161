
import numpy as np
from sklearn.base import BaseEstimator, is_classifier
from sklearn.model_selection import GridSearchCV, KFold

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data
X = np.random.rand(9, 2)  # Dummy feature data with 9 samples
y = np.random.randint(0, 2, 9)  # Dummy labels

# Define custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Create custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for the model
params = {'alpha': [0.1, 1.0, 10.0]}  # Example parameter grid

# Create a GridSearchCV instance
clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
