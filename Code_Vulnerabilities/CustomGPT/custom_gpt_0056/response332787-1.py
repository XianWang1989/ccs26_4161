
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Create a sample dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Instantiate the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define model and parameters for GridSearch
params = {'C': [0.1, 1, 10]}
clf = GridSearchCV(LogisticRegression(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output best parameters
print("Best parameters found:", clf.best_params_)
