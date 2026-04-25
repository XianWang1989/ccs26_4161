
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Example data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your own indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create your custom cross-validator
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define your model and parameters
clf = LogisticRegression()
param_grid = {'C': [0.1, 1, 10]}

# Use GridSearchCV with the custom cross-validator
grid_search = GridSearchCV(clf, param_grid, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Output best parameters found
print("Best parameters:", grid_search.best_params_)
