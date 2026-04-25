
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import BaseCrossValidator

# Custom CV class
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X, y = make_classification(n_samples=9, n_features=20, random_state=42)

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Initialize a classifier
clf = SVC()

# Define parameters for GridSearch
params = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}

# Run GridSearch with custom CV
grid_search = GridSearchCV(estimator=clf, param_grid=params, cv=custom_cv)
grid_search.fit(X, y)

print("Best parameters found: ", grid_search.best_params_)
