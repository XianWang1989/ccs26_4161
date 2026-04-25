
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Create instance of custom Cross-Validator
custom_cv = CustomCV(train_indices, test_indices)

# Specify parameters for Grid Search
params = {
    'n_estimators': [10, 50],
    'max_depth': [None, 5, 10]
}

# Initialize the classifier
clf = RandomForestClassifier(random_state=42)

# Set up GridSearchCV with custom CV
grid_search = GridSearchCV(clf, params, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Display best parameters
print("Best parameters found:", grid_search.best_params_)
