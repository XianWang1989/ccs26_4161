
from sklearn.model_selection import BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# Create synthetic data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Set up the GridSearchCV
params = {'max_depth': [1, 2, 3]}
clf = GridSearchCV(DecisionTreeClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

print("Best parameters found: ", clf.best_params_)
