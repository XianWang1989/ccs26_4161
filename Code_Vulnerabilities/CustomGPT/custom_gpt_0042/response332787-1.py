
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import make_classification
import numpy as np

# Step 1: Create custom cross-validation class
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Step 2: Generate some data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Step 3: Define your custom train-test splits
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Step 4: Instantiate your custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Step 5: Set up GridSearchCV
params = {'example_param': [0.1, 0.5, 1.0]}  # Example parameter for tuning
classifier = BaseEstimator()  # Replace with your actual classifier

grid_search = GridSearchCV(classifier, params, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# View results
print(grid_search.best_params_)
print(grid_search.best_score_)
