
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example Data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([1, 2, 1, 2, 1, 2, 1, 2, 1])

# Custom train and test indices for 2-fold CV
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]  # 0-based indexing
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of CustomCV
custom_cv = CustomCV(train_indices, test_indices)

# Define your model parameters
params = {'param1': [1, 2], 'param2': [0.01, 0.1]}

# Use GridSearchCV with the custom cross-validation iterator
clf = GridSearchCV(estimator=MyModel(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Display the results
print(clf.best_params_)
print(clf.best_score_)
