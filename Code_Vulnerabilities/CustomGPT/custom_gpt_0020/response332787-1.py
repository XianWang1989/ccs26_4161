
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin, is_classifier
from sklearn.model_selection import BaseCrossValidator

# Define a custom cross-validation class
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Sample data
X = np.array([[1], [2], [3], [4],[5],[6],[7],[8],[9]])
y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1])

# Define train and test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Instantiate custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Example model and parameter grid
from sklearn.linear_model import LogisticRegression

params = {'C': [0.1, 1, 10]}
clf = GridSearchCV(LogisticRegression(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Display the best parameters found
print("Best parameters:", clf.best_params_)
